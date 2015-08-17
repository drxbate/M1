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
				
				$(e).unbind("click");
				$(e).bind("click",function(){
					var control=this;
					var selector = $(e).attr("selector");
					showDialog("/selector/"+selector,{
							width:600,
							height:400,
							closed:function(value){
								var dis = $(control).attr("display-of-control");
								if(dis){$(dis).val(value.dispName);}else{$(control).val(value.dispName);}
								var val = $(control).attr("value-of-control");
								if(val){$(val).val(value.value);}else{$(control).val(value.value);}
								
							}
						});
				});
				
			});
		}
});