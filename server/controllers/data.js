const dataRouter = require('express').Router()
const Datapoint = require('../models/datapoint')

//GET
//#region
dataRouter.get('/time', (req, res) => {
  var date = new Date()
  res.json(date.toISOString())
})

dataRouter.get('/:t1([0-9]{4}*)/:t2([0-9]{4}*)', async (req, res) => {
  try{
    time1 = new Date(req.params.t1)
    time2 = new Date(req.params.t2)
    datapoints = await Datapoint.find({'timestamp':{'$gte':time1, '$lte':time2}})

    if(datapoints){
      res.json(datapoints.map(Datapoint.formatDatapoint))
    }else{
      res.status(404).end()
    }
  }catch(err){
    console.log(err)
    res.status(400).send({error: 'invalid timestamp'})
  }
})
//#endregion

module.exports = dataRouter
