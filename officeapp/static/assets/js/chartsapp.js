function chart_one(chart1,categories1){
  console.log(chart1)
  console.log(categories1)
  var a=[]
  chart1.forEach(item => {
    a.push({name:item[0],
      data:item[1]})             
    })
var options = {
    series: a,
    chart: {
    height: 550,
    toolbar: {show: false},
    type: 'line',
    zoom: {
      enabled: false
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    width: [5, 7, 5],
    curve: 'straight',
    dashArray: [0, 8, 5]
  },
  title: {
    text: 'Page Statistics',
    align: 'left'
  },
  legend: {
    tooltipHoverFormatter: function(val, opts) {
      return val + ' - ' + opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] + ''
    }
  },
  markers: {
    size: 0,
    hover: {
      sizeOffset: 6
    }
  },
  xaxis: {
    categories: categories1,
  },
  tooltip: {
    y: [
      {
        title: {
          formatter: function (val) {
            return val 
          }
        }
      },
      {
        title: {
          formatter: function (val) {
            return val 
          }
        }
      },
      {
        title: {
          formatter: function (val) {
            return val;
          }
        }
      }
    ]
  },
  grid: {
    borderColor: '#f1f1f1',
  }
  };

  var chart = new ApexCharts(document.querySelector("#chart1"), options);
  chart.render();
}


function chart_two(chart2){
   var options = {

      pie: {
        expandOnClick: false
      }
    ,
     series: chart2[0],
     chart: {
      toolbar: {show: false},
     height: 300,
     dataLabels: {
      enabled: true,
      },
     
     type: 'pie',
     pieSliceText: 'value'
   },
   labels: chart2[1],
   responsive: [{
     breakpoint: 480,
     options: {
       chart: {
         width: 200
       },
       legend: {
         position: 'bottom'
       }
     }
   }]
   };

   var chart = new ApexCharts(document.querySelector("#chart2"), options);
   chart.render();
}
function chart_three(chart3,categories3){
  var a=[]
  chart3.forEach(item => {
      a.push({name:item[0],
             data:item[1]})
  })
  var options = {
    series: a,
    chart: {
      height: 300,
      toolbar: {show: false},
      type: 'area',
      toolbar: {
        show: false
      },
    },
    markers: {
      size: 4
    },
    colors: ['#800080','#00FF00','#800000','#BC8F8F','#0000FF','#D8BFD8','#9ACD32','#FF1493','#008000','#D2691E','#FFD700','#5F9EA0','#00FFFF','#808000','#000080','#7B68EE','#DA70D6','#FF7F50','#FFFF00','#6E6E6E','#088A85','#2EFEF7','#58FA58','#610B0B','#170B3B'],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 1,
        opacityFrom: 0.3,
        opacityTo: 0.4,
        stops: [0, 90, 100]
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 2
    },
    xaxis: {
      type: 'time',
      categories: categories3
    },
    yaxis:{
      labels: {
        formatter: function (value) {
          return value;
        }
      }                
    },
    tooltip: {
      x: {
        format: 'HH'
      },
    }
  };
  var chart = new ApexCharts(document.querySelector("#chart3"), options);
  chart.render();
}





function chart_four(chart4,categories4){
  var a=[]
  chart4.forEach(item => {
      a.push({name:item[0],
             data:item[1]})
  })


     var options = {
       series: a,
       chart: {
       type: 'bar',
       toolbar: {show: false},
       height: 350
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '55%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 2,
       colors: ['transparent']
     },
     xaxis: {
       categories: categories4,
     },
     yaxis: {
       title: {
         text: 'abcd'
       }
     },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return  val 
         }
       }
     }
     };

     var chart = new ApexCharts(document.querySelector("#chart4"), options);
     chart.render();
}

function chart_five(chart5,categories5){
  var a=[]
  chart5.forEach(item => {
      a.push({name:item[0],
             data:item[1]})
  })


     var options = {
       series: a,
       chart: {
       type: 'bar',
       toolbar: {show: false},
       height: 350
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '55%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 2,
       colors: ['transparent']
     },
     xaxis: {
       categories: categories5,
     },
     yaxis: {
       title: {
         text: 'abcd'
       }
     },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return  val 
         }
       }
     }
     };

     var chart = new ApexCharts(document.querySelector("#chart5"), options);
     chart.render();
}

function chart_six(chart6,categories6){
  var a=[]
  chart6.forEach(item => {
      a.push({name:item[0],
             data:item[1]})
  })


     var options = {
       series: a,
       chart: {
       type: 'bar',
       toolbar: {show: false},
       height: 350
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '55%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 2,
       colors: ['transparent']
     },
     xaxis: {
       categories: categories6,
     },
     yaxis: {
       title: {
         text: 'abcd'
       }
     },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return  val 
         }
       }
     }
     };

     var chart = new ApexCharts(document.querySelector("#chart6"), options);
     chart.render();
}


function chart_seven(chart7,categories7){
  var a=[]
  chart7.forEach(item => {
      a.push({name:item[0],
             data:item[1]})
  })

     var options = {
       series: a,
       chart: {
       type: 'bar',
       toolbar: {show: false},
       height: 350
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '55%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 2,
       colors: ['transparent']
     },
     xaxis: {
       categories: categories7,
     },
     yaxis: {
       title: {
         text: 'abcd'
       }
     },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return  val 
         }
       }
     }
     };

     var chart = new ApexCharts(document.querySelector("#chart7"), options);
     chart.render();
}


function chart_eight(chart8,categories8){
  var a=[]
  chart8.forEach(item => {
      a.push({name:item[0],
             data:item[1]})
  })

     var options = {
       series: a,
       chart: {
       type: 'bar',
       toolbar: {show: false},
       height: 350
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '55%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 2,
       colors: ['transparent']
     },
     xaxis: {
       categories: categories8,
     },
     yaxis: {
       title: {
         text: 'abcd'
       }
     },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return  val 
         }
       }
     }
     };

     var chart = new ApexCharts(document.querySelector("#chart8"), options);
     chart.render();
}

