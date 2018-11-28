queue()
.defer(d3.json, "/chart/time_spent/")
   .await(deriveGraphs);
    
function deriveGraphs(error, data) {
    var ndx = crossfilter(data);
        data.forEach(function (d) {
        
    //format todays date for use in ongoing activities calcs     
    var today =new Date();
    var strtoday = today.toString(); 
    
    // format dates used in duration calcs
        d.created_date = new Date(d.created_date);
        d.completed_date = new Date(d.completed_date);
        d.assigned_date = new Date(d.assigned_date);
        d.today = new Date(strtoday);
        
        //calculate time intervals for use in duration calcs for pending and completed issues
        d.pending_dur_days = ((d.today - d.created_date)/(1000*60*60*24)); //day
        d.completed_dur_mins = ((d.completed_date - d.assigned_date)/(1000*60)); //minutes
        d.completed_dur_hours = ((d.completed_date - d.assigned_date)/(1000*60*60));//hours
        d.completed_dur_days = ((d.completed_date - d.assigned_date)/(1000*60*60*24)); //day
        //assume 7.02 days in a week (4 year period)
        d.completed_dur_weeks = ((d.completed_date - d.assigned_date)/(1000*3600*24*7));//weeks
        //assume 30.44 days in a month (4 year period)
        d.completed_dur_months = ((d.completed_date - d.assigned_date)/(1000*3600*24*7*30.44));//months
        
        //calculate time intervals for use in duration calcs for ongoing issues
        d.ongoing_dur_mins = ((d.today - d.assigned_date)/(1000*60)); //minutes
        d.ongoing_dur_hours = ((d.today - d.assigned_date)/(1000*60*60));//hours
        d.ongoing_dur_days = ((d.today - d.assigned_date)/(1000*60*60*24)); //day
        //assume 7.02 days in a week (4 year period)
        d.ongoing_dur_weeks = ((d.today - d.assigned_date)/(1000*3600*24*7));//weeks
        //assume 30.44 days in a month (4 year period)
        d.ongoing_dur_months = ((d.today - d.assigned_date)/(1000*3600*24*7*30.44));//month
       
    });

 // call graphing functions to render charts       
    dist_to_date(ndx);
    stat_by_cat(ndx);
    upvote_by_cat(ndx);
    days_by_cat(ndx);
    days_by_cat_ongoing(ndx);
    items_pending(ndx);
    show_pie_fees(ndx);
    dc.renderAll();
  
}

function dist_to_date(ndx) {
    var dim = ndx.dimension(dc.pluck('category'));
    var group = dim.group();
// bar chart showing total bugs and features to date
    dc.barChart("#all_issues")
        .width(300)
        .height(400)
        .margins({top: 50, right: 50, bottom: 40, left: 50})
        .dimension(dim)
        .group(group)
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .title(function(d) { return d.key +" quantity is "+ d.value; })
        .xAxisLabel("Category")
        .yAxisLabel("Quantity")
        .yAxis().ticks(10);
    
}
//bar chart showing status of bugs and features
function stat_by_cat(ndx) {
    var cat_dim = ndx.dimension(dc.pluck('status'));
            function totBug(Bug) {
                return function (d) {
                    d.count = 0;
                   if (d.category === "Bug") {
                     d.count++;
                     return d.count;
                 } else {
                     return 0;
                 } 
                };
            }
    var    totalBug = cat_dim.group().reduceSum(totBug('Bug'));
        function totFeature(Feature) {
            return function (d) {
                d.count = 0;
               if (d.category === "Feature") {
                 d.count++;
                 return d.count;
             } else {
                 return 0;
             } 
            };
        }
    var    totalFeature = cat_dim.group().reduceSum(totFeature('Feature'));

    dc.barChart("#stack_status")
        .width(300)
        .height(400)
        .margins({top: 50, right: 50, bottom: 40, left: 50})
        .dimension(cat_dim)
        .group(totalBug, 'Bug')
        .stack(totalFeature, 'Feature')
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .title(function(d) { return d.key +" quantity is "+ d.value; })
         .legend(dc.legend().x(10).y(10).itemHeight(10).gap(3))
        .xAxisLabel("Status")
        .yAxisLabel("Quantity")
        .yAxis().ticks(10);
        
}
//bar chart showing upvotes by category
function upvote_by_cat(ndx) {
    var cat_dim = ndx.dimension(dc.pluck('category'));
    var tot_upvotes = cat_dim.group().reduceSum(dc.pluck('upvotes'));  
    dc.barChart("#upvote_status")
        .width(300)
        .height(400)
        .margins({top: 50, right: 50, bottom: 40, left: 50})
        .dimension(cat_dim)
        .group(tot_upvotes)
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .title(function(d) { return d.key +" quantity is "+ d.value; })
        .xAxisLabel("Category")
        .yAxisLabel("Upvotes")
        .yAxis().ticks(10);
        
}
//bar chart showing time spent on issues by category status completed
 function days_by_cat(ndx) {
    function days_for_completed(category) {
                return function (d) {
                  if (d.status === 'Completed') {
                     return +d.completed_dur_days;
                 } else {
                     return 0;
                 } 
                };
            }
    var cat_dim = ndx.dimension(dc.pluck('category'));
    var tot_cat_days = cat_dim.group().reduceSum(days_for_completed('Completed'));  
    dc.barChart("#days_by_cat")
        .width(300)
        .height(400)
        .margins({top: 50, right: 50, bottom: 40, left: 50})
        .dimension(cat_dim)
        .group(tot_cat_days)
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .title(function(d) { return d.key +" quantity is "+ d.value; })
        .xAxisLabel("Category Status Completed")
        .yAxisLabel("Number of days")
        .yAxis().ticks(10);
        
}
//bar chart showing time spent on issues by category status ongoing
 function days_by_cat_ongoing(ndx) {
    function days_for_ongoing(category) {
                return function (d) {
                  if (d.status === 'Ongoing') {
                     return +d.ongoing_dur_days;
                 } else {
                     return 0;
                 } 
                };
            }
    var cat_dim = ndx.dimension(dc.pluck('category'));
    var tot_cat_days = cat_dim.group().reduceSum(days_for_ongoing('Ongoing'));  
    dc.barChart("#days_by_cat_ongoing")
        .width(300)
        .height(400)
        .margins({top: 50, right: 50, bottom: 40, left: 50})
        .dimension(cat_dim)
        .group(tot_cat_days)
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .title(function(d) { return d.key +" quantity is "+ d.value; })
        .xAxisLabel("Category Status Ongoing")
        .yAxisLabel("Number of days")
        .yAxis().ticks(10);
        
}
//bar chart showing how many days items are pending
 function items_pending(ndx) {
    function days_for_pending(category) {
                return function (d) {
                  if (d.status === 'Pending') {
                     return +d.pending_dur_days;
                 } else {
                     return 0;
                 } 
                };
            }
    var cat_dim = ndx.dimension(dc.pluck('category'));
    var tot_cat_days = cat_dim.group().reduceSum(days_for_pending('Pending'));  
    dc.barChart("#days_pending")
        .width(300)
        .height(400)
        .margins({top: 50, right: 50, bottom: 40, left: 50})
        .dimension(cat_dim)
        .group(tot_cat_days)
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .title(function(d) { return d.key +" quantity is "+ d.value; })
        .xAxisLabel("Duration of Pending Items")
        .yAxisLabel("Number of days")
        .yAxis().ticks(10);
        
}
//pie chart showing percentage of fees recieved for features by status
function show_pie_fees(ndx) {
    var statusColors = d3.scale.ordinal()
        .domain(["Completed", "Ongoing", "Pending"])
        .range(["#5cb85c", "Beige", "Pink"]);
    var dim = ndx.dimension(dc.pluck('status'));
    function feature_fees() {
                return function (d) {
                  if (d.category === 'Feature') {
                     return +d.fee;
                 } else {
                     return 0;
                 } 
                };
            }
    var feesGroup = dim.group().reduceSum(feature_fees());
    dc.pieChart("#fee-pie-chart")
        .height(300)
        .radius(150)
        .transitionDuration(1500)
        .colors(statusColors)
        .dimension(dim)
        .group(feesGroup)
        .legend(dc.legend().x(100).y(0).itemHeight(13).gap(5))
        .renderlet(function(chart){
    chart.selectAll('text.pie-slice').text( function(d) {
    return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });
}  
 queue()
        .defer(d3.json, "/chart/weekly/")
        .await(makeGraphs);
     
        function makeGraphs(error, weeklyData) {
            var ndx = crossfilter(weeklyData);
            //console.log(Data);
           
             weeklyData.forEach(function(d) {
                 d.upvotes = +d.upvotes;
           
             });
             
 show_weekly_act(ndx);
    dc.renderAll();
  
} 
function show_weekly_act(ndx) {
    var cat_dim = ndx.dimension(dc.pluck('category'));
        function allStatus(status) {
             return function (d) {
                 d.count = 0;
                 if (d.status === status) {
                     d.count++;
                     return d.count;
              }  else {
                     return 0;
              } 
             };
         }   
    var totalComp = cat_dim.group().reduceSum(allStatus('Completed'));    
         dc.pieChart("#completed-weekly-chart")
            .height(330)
            .radius(150)
            .transitionDuration(1500)
            .dimension(cat_dim)
            .group(totalComp)
            //.legend(dc.legend().x(20).y(20).itemHeight(13).gap(5))
            .renderlet(function(chart){
            chart.selectAll('text.pie-slice').text( function(d) {
            return 'Completed' + ' ' + d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });    
         
    var totalOng = cat_dim.group().reduceSum(allStatus('Ongoing'));          
         dc.pieChart("#ongoing-weekly-chart")
            .height(330)
            .radius(150)
            .transitionDuration(1500)
            .dimension(cat_dim)
            .group(totalOng)
            //.legend(dc.legend().x(20).y(20).itemHeight(13).gap(5))
            .renderlet(function(chart){
            chart.selectAll('text.pie-slice').text( function(d) {
            return 'Ongoing' + ' ' + d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        });
    });     
         
         
         
}