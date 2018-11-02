import React from "react";
import Measurements from './components/measurements.js'
import Chart from './components/chart.js'
import Datapoint from './services/datapoint.js'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      datapoints: {}
    }
  }

  data = {
    datasets:[{
      label: 'Temperature',
      showLine: 'true',
      data: []
    }]
  }
  dataAvailable = false

  update = () => {
      Datapoint.getLatest().then(res => {
        const newpoint = {
          t: Date(res.timestamp),
          y: res.value
        }
        this.data.datasets[0].data.push(newpoint)
        this.setState({
            datapoints: this.data
        })
      })
  }
  componentDidMount() {setInterval(this.update,1000)}

  render() {
    return (
      <div>
        <h2>Velocity measurement</h2>
        <Measurements measurements={this.state.datapoints}/>
        <Chart data={this.state.datapoints}/>
      </div>
    );
  }
}

export default App;
