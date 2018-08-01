var margin = {top: 40, right: 30, bottom: 50, left: 60},
    width = 0.8 * document.getElementById("graph").offsetWidth - margin.right - margin.left,
    height = 0.5 * width;

//bisector returns an index of the array
var bisectX = d3.bisector(function(d) { return d.x; }).left;

var x = d3.scale.linear()
    .range([0, width])
    .domain([0, 100]);

var y = d3.scale.linear()
    .range([height, 0])
    .domain([0, (d3.max(flowjson, function(d) {return d.y;})*1.2)]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")

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
        .ticks(11)
};

//Graph boundaries
var svg = d3.select("svg")
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
      )

svg.append("g")
    .attr("class", "grid")
    .call(make_y_axis()
        .tickSize(-width, 0, 0)
        .tickFormat("")
    )


//Define lines
var flowline = d3.svg.line()
  .x(function(d) { return x(d.x); })
  .y(function(d) { return y(d.y); });

//Draw lines on graph
svg.append("path")
    .attr("class", "line")
    .style("stroke", "red")
    .attr("d", flowline(flowjson));

//x-axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .append("text")
      .attr("x", (width / 2 - 30 ))
      .attr("y", 35)
      .style("font-size", "12px")
      .text("Reliability (%)");

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
    .text("Discharge (cumecs)");

//Chart title
svg.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top / 2) + 10)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .text(graphtitle + " streamflow reliability");


var focus = svg.append("g")
    .style("display", "none");

focus.append("text")
    .attr("x", 15)
  	.attr("dy", ".31em");

focus.append("circle")
    .style("fill", "none")
    .style("stroke", "blue")
    .attr("r", 4);

svg.append("rect")
    .attr("width", width)
    .attr("height", height)
    .style("fill", "none")
    .style("pointer-events", "all")
    .on("mouseover", function() { focus.style("display", null); })
    .on("mouseout", function() { focus.style("display", "none"); })
    .on("mousemove", mousemove);

function mousemove() {
    var x0 = x.invert(d3.mouse(this)[0]),
        i = bisectX(flowjson, x0, 1),
        d0 = flowjson[i - 1],
        d1 = flowjson[i];
        d = x0 - d0.x > d1.x - x0 ? d1 : d0;

    focus.attr("transform","translate(" + x(d.x) + "," + y(d.y) + ")");
    focus.select("text").text(d.y + " cumecs");

};
