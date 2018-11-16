queue()
.defer(d3.json, "/chart/bugs/")
   .await(deriveGraphs);
   
   function deriveGraphs(error, data) {
        var ndx = crossfilter(data);
        data.forEach(function (d) {

    });
     //call functions to render graphs
    show_pie_status(ndx);
    dc.renderAll();
  
}
function show_pie_status(ndx) {
    var dim = ndx.dimension(dc.pluck('status'));
    var group = dim.group();
        dc.pieChart("#bug-chart")
                .height(350)
                .radius(150)
                .transitionDuration(1500)
                .dimension(dim)
                .group(group)
                .legend(dc.legend().x(100).y(0).itemHeight(13).gap(5))
                .renderlet(function(chart){
        chart.selectAll('text.pie-slice').text( function(d) {
        return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
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
     //call functions to render graphs
    show_feat_status(ndx);
    dc.renderAll();
  
}
function show_feat_status(ndx) {
    var dim = ndx.dimension(dc.pluck('status'));
    var group = dim.group();
        dc.pieChart("#feature-chart")
                .height(350)
                .radius(150)
                .transitionDuration(1500)
                .dimension(dim)
                .group(group)
                .legend(dc.legend().x(100).y(0).itemHeight(13).gap(5))
                .renderlet(function(chart){
        chart.selectAll('text.pie-slice').text( function(d) {
        return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });
}