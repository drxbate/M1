/*
 * 选择器控件
 * 
 * 显示选择器 /selector/<模块名>，用户点选选择器获取显示内容及值。
 * 
 * e.g.
  <input type="text" 			 
			selector="district" //选择模块 /selector/<模块名>
			display-of-control="#hidDistrict" //内容显示控件 $(...)，如果无该属性，则存放 内容显示控件
			value-of-control="#hidDistrict" //数据存放控件 $(...)，如果无该属性，则默认当前控件为 数据存放控件
			>
			<input type="hidden" id="hidDistrict" />
 */
$.fn.extend({
		bindSelector:function(){
			$(this).find(".selector").each(function(i,e){
				if($(e).attr("data-init")!="1"){
					var ig=$("<div class='input-group'></div>");
					$(e).wrap(ig);
					var container=$(e).parent();
					
					container.append($("<div class='input-group-addon'><span class='fa fa-th-list' style='font-size:12pt;'></span></div>"));
					
					$(e).attr("data-init","1");
					container.unbind("click");
					container.bind("click",function(){
						var control=$(this).find(".selector");
						var selector = $(e).attr("selector");
						var parameter = $(e).attr("selector-parameter");
						showDialog("/selector/"+selector+"?"+parameter,{
								width:600,
								height:400,
								closed:function(value){
									$(control).val(value.dispName);
									var val = $(control).attr("value-of-control");
									if(val){$(val).val(value.value);}else{$(control).val(value.value);}
									
								}
							});
					});
				}
			});
		}
});