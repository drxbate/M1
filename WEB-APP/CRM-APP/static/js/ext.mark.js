/*
 * mark 标签 容器
 * 
 * 显示已经选中标签，以及添加新标签
 * 
 * e.g.
 
 */
$.fn.extend({
		initMark:function(){
			$(this).find(".mark-container").each(function(i,e){
				var marks=[];
				$(".mark").each(function(i,e){
					var role=$(e).attr("role");
					var data=$(e).attr("data");
					if(role=="icon"){
						$(e).addClass("mark-icon-"+data);
					}
				});
			});
			
			$(this).find(".mark-container").bind("click",function(){
				showDialog("/selector/mark");
			});
		}
});