var margin = {top: 80, right: 30, bottom: 30, left: 50},
    width = 0.8 * document.getElementById("wellgraph").offsetWidth - margin.left - margin.right,
    height = 0.5 * width;

var parseDate = d3.time.format("%m/%d/%Y").parse;

var startdate = parseDate(welljson[11]["x"]),
    enddate = parseDate(welljson[0]["x"]);

var x = d3.time.scale()
    .range([0, width])
    .domain([startdate, enddate]);

var y = d3.scale.linear()
    .range([0, height])
    .domain([0, (d3.max(welljson, function(d) {return d.y;}) + 10)]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("top")
    .ticks(11)
    .tickFormat(d3.time.format("%b-%Y"));

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

//Grid functions
function make_x_axis() {
    return d3.svg.axis()
        .scale(x)
        .orient("bottom")
        .ticks(11)
};

function make_y_axis() {
    return d3.svg.axis()
        .scale(y)
        .orient("left")
};

//Graph boundaries
var svg = d3.select("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//Grid
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

//Draw line on graph
var wellline = d3.svg.line()
  .x(function(d) { return x(parseDate(d.x));})
  .y(function(d) { return y(d.y);});

svg.append("path")
    .attr("class", "line")
    .style("stroke", "red")
    .attr("d", wellline(welljson));

//Area fill
// var area = d3.svg.area()
//     .x(function(d) { return x(parseDate(d.x));})
//     .y0(height)
//     .y1(function(d) { return y(d.y); });
//
// svg.append("path")
//     .datum(welljson)
//     .attr("fill", "steelblue")
//     .attr("d", area);

//x-axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0, 0)")
    .call(xAxis);

//y-axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 5 - margin.left)
    .attr("x",0 - (height / 2))
    .attr("dy", "1em")
    .style("font-size", "12px")
    .text("Reduced level (m)");

//Chart title
svg.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .text(graphtitle + " Reduced Level");

//legend
// svg.append("g")
//     .attr("class","legend")
//     .attr("transform","translate(50,30)")
//     .style("font-size","12px")
//     .call(d3.legend);
