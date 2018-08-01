var margin = {top: 40, right: 30, bottom: 50, left: 60},
  //Width and height of graph
    width = 0.8 * document.getElementById("idfcontainer").offsetWidth - margin.right - margin.left,
    height = 0.5 * width;

var x = d3.scale.log()
    .range([0, width])
    .domain([5, 2000]);

var y = d3.scale.log()
    .range([height, 0])
    .domain([1, 500]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .tickFormat(function (d) {
      return x.tickFormat(10,d3.format(",d"))(d)
    });

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(function (d) {
      return y.tickFormat(10,d3.format(",d"))(d)
    });

function make_x_axis() {
    return d3.svg.axis()
        .scale(x)
        .orient("bottom")
        .ticks(10)
};

function make_y_axis() {
    return d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10)
};

//Graph boundaries
var svg = d3.select("#idfsvg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//grid
svg.append("g")
      .attr("class", "grid")
      .attr("transform", "translate(0," + height + ")")
      .call(make_x_axis()
          .tickSize(-height, 0, 0)
          .tickFormat("")
      );

svg.append("g")
    .attr("class", "grid")
    .call(make_y_axis()
        .tickSize(-width, 0, 0)
        .tickFormat("")
    );

//Python json to javascript friendly :)
var twoyearraw = [];
var fiveyearraw = [];
var tenyearraw = [];
var tfyearraw = [];
var fiftyyearraw = [];
var hundredyearraw = [];

//idfjsonObject is passed from html, which is passed from the view.
Object.keys(idfjsonObject).forEach(function(key) {
  twoyearraw.push([key, idfjsonObject[key][0]]);
  fiveyearraw.push([key, idfjsonObject[key][1]]);
  tenyearraw.push([key, idfjsonObject[key][2]]);
  tfyearraw.push([key, idfjsonObject[key][3]]);
  fiftyyearraw.push([key, idfjsonObject[key][4]]);
  hundredyearraw.push([key, idfjsonObject[key][5]])
});

//D3 graph datasets
var twoyeardata = twoyearraw.map(function(d) {
    return {
      x: d[0],
      y: d[1]
    };
});

var fiveyeardata = fiveyearraw.map(function(d) {
    return {
      x: d[0],
      y: d[1]
    };
});

var tfyeardata = tfyearraw.map(function(d) {
    return {
      x: d[0],
      y: d[1]
    };
});

var hundredyeardata = hundredyearraw.map(function(d) {
    return {
      x: d[0],
      y: d[1]
    };
});


//Define lines
var twoyearline = d3.svg.line()
  .x(function(d) { return x(d.x); })
  .y(function(d) { return y(d.y); });

var fiveyearline = d3.svg.line()
  .x(function(d) { return x(d.x); })
  .y(function(d) { return y(d.y); });

var tfyearline = d3.svg.line()
  .x(function(d) { return x(d.x); })
  .y(function(d) { return y(d.y); });

var hundredyearline = d3.svg.line()
  .x(function(d) { return x(d.x); })
  .y(function(d) { return y(d.y); });

//Draw lines on graph
svg.append("path")
    .attr("class", "line")
    .attr("data-legend", "Two Year")
    .attr("d", twoyearline(twoyeardata));

svg.append("path")
    .attr("class", "line")
    .style("stroke", "green")
    .attr("data-legend", "Five Year")
    .attr("d", fiveyearline(fiveyeardata));

svg.append("path")
    .attr("class", "line")
    .style("stroke", "brown")
    .attr("data-legend", "Twenty-Five Year")
    .attr("d", tfyearline(tfyeardata));

svg.append("path")
    .attr("class", "line")
    .style("stroke", "red")
    .attr("data-legend", "Hundred Year")
    .attr("d", hundredyearline(hundredyeardata));

//x-axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .append("text")
      .attr("x", (width / 2 - 30 ))
      .attr("y", 35)
      .style("font-size", "12px")
      .text("Duration (min)");

//y-axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 5)
      .attr("x", 0 - (height / 2) - 30)
      .attr("dy", "1em")
      .style("font-size", "12px")
      .text("Intensity (mm/hr)");

//Chart title
svg.append("text")
      .attr("x", (width / 2))
      .attr("y", 0 - (margin.top / 2))
      .attr("text-anchor", "middle")
      .style("font-size", "16px")
      .style("text-decoration", "underline")
      .text("Intensity-Duration-Frequency curves for " + graphtitle);

//legend
svg.append("g")
    .attr("class","legend")
    .attr("transform", "translate(" + (width - margin.right - 100) + ", 20)")
    .style("font-size","12px")
    .call(d3.legend);
