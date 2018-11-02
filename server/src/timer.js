const Datapoint = require('../models/datapoint')
const LSM9DS1 = require('../drivers/LSM9DS1')
const filter = require('./filter')

measRate = 100      //ms
sampling = 1/80*1000//ms
intervalStop = 1600/sampling //5km/h
minDeltaT = 0.131946891//s ~ 64.8km/h
stop = false

baseline = LSM9DS1.readMagnetometer()
threshold = 0.03

diameter = 0.7

latestDatapoint = null

values = 0
times = [0,0]
peak = 0
intervals = 0
intervalsPrev = 0

function detectPeak(){
  interval = setInterval(function samples(){
    n = LSM9DS1.readMagnetometer()
    //Inside the "baseline zone"
    if(n < baseline * (1+threshold) && n > baseline * (1-threshold) && peak == 1){
      peak = 0
    }
    //Inside the "peak zone"
    else if(n > baseline * (1+threshold) || n < baseline * (1-threshold) && peak == 0){    
      clearInterval(interval)

      peak = 1
      intervalsPrev = intervals
      intervals = 0

      times[values] = new Date()
      
      //We have two timestamps, calculate velocity
      if(values === 1){
        //Low speeds (<6 km/h) often resulted in 64.89 km/h because deltaT ~ 120ms (measRate + sampling)
        //deltaT of 0.131946891 = 60km/h
        if((times[1].getTime() - times[0].getTime())/1000 < minDeltaT){
          if(latestDatapoint.value > 55){
            saveVelocity(calculateVelocity())
          }else{
            reset()
          }
        }else{
          saveVelocity(calculateVelocity())
        }
      }
      else{values++}

      timer = setTimeout(detectPeak,measRate)
    }
    //If a peak was not detected within n samples, save 0 and reset
    else if(++intervals > intervalStop){
      saveVelocity(0)
      reset()
    }
    if(stop){clearInterval(interval)}
  },sampling)
}

function reset(){
  values = 0
  intervals = 0
  times = [0, 0]
}

function turnOn(){
  latestDatapoint = Datapoint.formatDatapoint({
    value: 0,
    timestamp: new Date()
  })
  stop = false
  timer = setTimeout(detectPeak, 0)
}

function turnOff(){
  stop = true
  LSM9DS1.turnOff();
}

function calculateVelocity(){
  deltaT = (times[1].getTime() - times[0].getTime())/1000
  velocity = (Math.PI * diameter) / deltaT * 3.6
  return velocity
}

function calculateStop(velocity){
  if(intervalsPrev === 0 || intervalsPrev > 60 || velocity === 0){
    intervalStop = intervalStop = 1600/sampling
  }else if(intervalsPrev < 10){
    intervalStop = 5 + intervalsPrev
  }else{
    intervalStop = 5 + Math.ceil(intervalsPrev * 1.4)
  }
}

function saveVelocity(velocity){
  velocity = filter.medianFilter(velocity)
  //console.log(intervalsPrev,intervalStop,velocity)
  calculateStop(velocity)
  latestDatapoint = Datapoint.formatDatapoint({
    value:velocity,
    timestamp: new Date()
  })

  const datapoint = new Datapoint(latestDatapoint).save()
  times[0] = times[1]
  times[1] = 0
}

getLatest = () => latestDatapoint
module.exports = {
  getLatest: getLatest,
  turnOn: turnOn,
  turnOff: turnOff
}