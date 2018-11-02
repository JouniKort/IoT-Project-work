const sensorRouter = require('express').Router()
const timer = require('../src/timer')

//#region PUT
sensorRouter.put('/', (req,res) => {
    if(req.body.sensor === 'on'){
        console.log('sensor on')
        timer.turnOn()
        res.send('On')
    }else{
        console.log('sensor off')
        timer.turnOff()
        res.send('Off')
    }
})
//#endregion

//#region GET
sensorRouter.get('/latest', (req,res) => {
    datapoint = timer.getLatest()
    if(datapoint){
      res.json(datapoint)
    }else{
      res.status(404).send({error: 'Latest value is null'})
    }
})
//#endregion

module.exports = sensorRouter
