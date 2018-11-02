const mongoose = require('mongoose')

if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config()
}

const url = process.env.MONGODB_URI

mongoose.connect(url)

const DatapointSchema = mongoose.Schema({
  timestamp: {type: Date, default: Date.now},
  value: Number
})

DatapointSchema.statics.formatDatapoint = function(datapoint){
  return {
    timestamp: datapoint.timestamp,
    value: datapoint.value,
    id: datapoint._id
  }
}

Datapoint = null

try{
  Datapoint = mongoose.model('Datapoint', DatapointSchema)
}catch(err){
  Datapoint = mongoose.model('Datapoint')
}

module.exports = Datapoint