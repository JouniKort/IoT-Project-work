import React from 'react'
import {Line} from 'react-chartjs-2'

const Chart = ({data}) => {
    console.log(data)
    return(
        <div className='chart'>
            <Line
            data={data}
            options= {{
                scales: {
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'second',
                            displayFormats:{
                                seconds: 'HH:mm:ss'
                            }
                        }
                    },]

                }
            }}/>
        </div>
    )
}

export default Chart