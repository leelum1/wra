var margin = {top: 40, right: 30, bottom: 30, left: 60},
    width = 0.8 * document.getElementById("graph").offsetWidth - margin.right - margin.left,
    height = 0.5 * width;

var parseDate = d3.time.format("%m/%d/%Y").parse;

var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

var startdate = parseDate(rainjson[11]["x"]),
    enddate = parseDate(rainjson[0]["x"]);

var x = d3.time.scale()
    .range([0, width])
    .domain([startdate, enddate]);

var y = d3.scale.linear()
    .range([height, 0])
    .domain([0, max_rain + 10]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(20)
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

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<span>" + months[parseDate(d.x).getMonth()] + " " + parseDate(d.x).getFullYear() + " : " + d.y + " mm</span>";
  });

//Graph boundaries
var svg = d3.select("svg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.call(tip);

//grid
svg.append("g")
    .attr("class", "grid")
    .call(make_y_axis()
        .tickSize(-width, 0, 0)
        .tickFormat("")
    )

//data
svg.selectAll("bar")
    .data(rainjson)
  .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) { return x(parseDate(d.x)); })
    .attr("width", 20)
    .attr("y", function(d) { return y(d.y); })
    .attr("height", function(d) { return height - y(d.y); })
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide);

//x-axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .append("text")
    .attr("x", width / 2 )
    .attr("y", height - margin.bottom)
    .attr("dy", "1em")
    .style("font-size", "12px")
    .text("Reliability");

//y-axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 10)
    .attr("x",0 - (height / 2))
    .attr("dy", "1em")
    .style("font-size", "12px")
    .text("Rainfall (mm)");

//Chart title
svg.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .text("Rainfall at " + graphtitle + " for the past 12 months");
