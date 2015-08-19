/*
 * mark 标签 容器
 * 
 * 显示已经选中标签，以及添加新标签
 * 
 * e.g.
 
 */
$.fn.extend({
		initMark:function(){
			var container=$(this).find(".mark-container")
			container.each(function(i,e){
				var marks=[];
				$(".mark").each(function(i,e){
					var role=$(e).attr("role");
					var data=$(e).attr("data");
					if(role=="icon"){
						$(e).addClass("mark-icon-"+data);
					}
				});
				var val=$(this).attr("value");
				$(this).setMarks(val);
			});
			
			container.bind("click",function(){
				var cls=$(this).attr("mark-class");
				showDialog("/selector/mark/"+cls,{
					load:function(win){
						var ll=[];
						$(".mark-container .mark").each(
								function(i,e){
									ll.push($(e).attr("mark-id"));
								}
						);
						win.select(ll);
					},
					closed:function(state){
						if(!state){
							return;
						}
						container.html("");
						var ll=[];
						$(state).each(function(i,e){
							container.append($(this).createMark(e));
							ll.push(e["mark-id"]);
						});
						container[0].value=ll.join(",");
					}
				});
			});
		},

		configMark:function(options){
			var e = $(this);
			e.find(".text").text(options["mark-text"]==""?"...":options["mark-text"]);
			e.removeClass().addClass("mark mark-style "+options["mark-style"]);
			e.find(".icon").removeClass().addClass("icon fa fa-"+options["mark-icon"]).css("color",options["mark-icon-color"]);
			e.attr("mark-id",options["mark-id"])
				.attr("mark-text",options["mark-text"])
				.attr("mark-style",options["mark-style"])
				.attr("mark-icon",options["mark-icon"])
				.attr("mark-icon-color",options["mark-icon-color"])
				.attr("mark-lock",options["mark-lock"]);
		},
		
		createMark:function(options){
			var e = $("<div class='mark'><span class='icon'></span><span class='text'></span></div>");
			if(options){
				e.configMark(options);
			}
			return e;
		},
		
		setMarks:function(marks){
			var cls=$(this).attr("mark-class");
			$.post("/selector/mark/"+cls+"/query",
					{"ids":marks},
					function(json){
						if(json.state==0){
							$(json.data,function(i,e){
									var opt={
										"mark-id":e["__id__"],
										"mark-text":e["text"],
										"mark-style":e["style"],
										"mark-icon":e["icon"],
										"mark-icon-color":e["iconColor"],
										};
									container.append($(this).createMark(opt));
									
							});
						}
					},
					"json"
			);
		}
});