queue()
.defer(d3.json, "/chart/bugs/")
   .await(deriveGraphs);
   
   function deriveGraphs(error, data) {
        var ndx = crossfilter(data);
        data.forEach(function (d) {
           
    });
    //for testing purposes print returned data to console
     console.log(data);

     //call function to render graph
    show_pie_status(ndx);
    dc.renderAll();
  
}
// bug pie chart showing status 
function show_pie_status(ndx) {
    var statusColors = d3.scale.ordinal()
        .domain(["Completed", "Ongoing", "Pending"])
        .range(["#8FBC8F", "#FAFAD2", "#FFB6C1"]);
    var dim = ndx.dimension(dc.pluck('status'));
    var group = dim.group();
        dc.pieChart("#bug-chart")
                .height(250)
                .radius(125)
                .colors(statusColors)
                .transitionDuration(1500)
                .dimension(dim)
                .group(group)
                .on("renderlet", function(chart) {
                    chart.selectAll('text.pie-slice').text( function(d) {
                    return 'Bugs' + ' ' + d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });
} 
queue()
.defer(d3.json, "/chart/features/")
   .await(makeGraphs);
   
   function makeGraphs(error, data) {
        var ndx = crossfilter(data);
        data.forEach(function (d) {
    
    });
     //for testing purposes print returned data to console
    console.log(data);

     //call function to render graph
    show_feat_status(ndx);
    dc.renderAll();
  
}
// feature pie chart showing status 
function show_feat_status(ndx) {
    var statusColors = d3.scale.ordinal()
        .domain(["Completed", "Ongoing", "Pending"])
        .range(["#8FBC8F", "#FAFAD2", "#FFB6C1"]);
    var dim = ndx.dimension(dc.pluck('status'));
    var Group = dim.group();
        dc.pieChart("#feature-chart")
                .height(250)
                .radius(125)
                .colors(statusColors)
                .transitionDuration(1500)
                .dimension(dim)
                .group(Group)
                .on("renderlet", function(chart) {
                    chart.selectAll('text.pie-slice').text( function(d) {
                    return 'Features' + ' ' + d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });
}
queue()
.defer(d3.json, "/chart/chart_issues/")
   .await(moreGraphs);
   
   function moreGraphs(error, data) {
        var ndx = crossfilter(data);
        data.forEach(function (d) {
    
    });
     //for testing purposes print returned data to console
    console.log(data);

     //call function to render graph
    show_bug_feat_ratio(ndx);
    dc.renderAll();
  
}
// pie chart showing ratio of bugs to features 
function show_bug_feat_ratio(ndx) {
    var statusColors = d3.scale.ordinal()
        .domain(["Feature", "Bug"])
        .range(["#0099CC", "#006699"]);
    var dim = ndx.dimension(dc.pluck('category'));
    var group = dim.group();
        dc.pieChart("#feature-bug")
                .height(250)
                .radius(125)
                .colors(statusColors)
                .transitionDuration(1500)
                .dimension(dim)
                .group(group)
                .on("renderlet", function(chart) {
                    chart.selectAll('text.pie-slice').text( function(d) {
                    return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });
}