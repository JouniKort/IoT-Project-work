import React from 'react'
import '../styles/table.css'

const Measurements = ({measurements}) => {
  if(measurements.datasets === undefined){return null}
  measurements = measurements.datasets[0].data
  if(measurements === ''){return null}
  else{
    return (
      <table>
        <thead>
          <tr>Timestamp</tr>
          <tr>Measurement</tr>
        </thead>
        <tbody>
          {measurements.map(meas => <Measurement measurement={meas}/>)}
        </tbody>
      </table>
    )
  }
}

const Measurement = ({measurement}) => {
  console.log(measurement.timestamp)
  return (
    <tr>
      <td>{measurement.t}</td>
      <td>{measurement.y}</td>
    </tr>
    )
}

export default Measurements