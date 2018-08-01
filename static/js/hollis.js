var margin = {top: 40, right: 30, bottom: 60, left: 60},
    width = 0.8 * document.getElementById("hollisdiv").offsetWidth - margin.right - margin.left,
    height = 0.5 * width;

var parseDate = d3.time.format("%m/%d/%Y").parse;

var startdate = parseDate(hollis[11]["x"]),
    enddate = parseDate(hollis[0]["x"]);

var x = d3.time.scale()
    .range([0, width])
    .domain([startdate, enddate]);

var y = d3.scale.linear()
    .range([height, 0])
    .domain([570, 630]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(12)
    .tickFormat(d3.time.format("%b-%Y"));

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")

function make_x_axis() {
    return d3.svg.axis()
        .scale(x)
        .orient("bottom")
        .ticks(12)
}

function make_y_axis() {
    return d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10)
}

//Graph boundaries
var svg = d3.select("#hollissvg")
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
    )

//Top Draw Off
var topdrawoffdata = 620

// var topdrawoffline = d3.svg.line()
//   .x(function(d) { return x(parseDate(d.x));})
//   .y(function(d) { return y(d.y);});
//
// svg.append("path")
//     .attr("class", "line")
//     .style("stroke", "red")
//     .attr("d", levelline(hollis));

//Reservoir Level
var levelline = d3.svg.line()
  .x(function(d) { return x(parseDate(d.x));})
  .y(function(d) { return y(d.y);});

svg.append("path")
    .attr("class", "line")
    .style("stroke", "red")
    .attr("d", levelline(hollis));

//x-axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", ".15em")
        .attr("transform", "rotate(-65)");

//y-axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 5 - margin.left)
    .attr("x", 0 - (height / 2) - 30)
    .attr("dy", "1em")
    .style("font-size", "12px")
    .text("Water Elevation (ft)");

//Chart title
svg.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .text("Hollis Reservoir Level");
