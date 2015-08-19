
function showDialog(url,options){	
	var _options={
			width:800,
			height:600,
			load:function(){},
			closed:function(state){
			}
	};
	$.extend(_options,options);
	var html = '<div class="modal fade" id="__dialog__" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">'
	  +'<div class="modal-dialog" role="document">'
	    +'<div class="modal-content">'
	      +'<div class="modal-body">'
	      +'<iframe src="'+url+'" style="border:0;width:100%"></iframe>'
	      +'</div>'
	    +'</div>'
	  +'</div>'
	+'</div>';
	var e = window.top.$(html);
	e.find(".modal-dialog").width(_options.width);
	e.find(".modal-body iframe").height(_options.height);
	e.modal("show");
	
	var closeMe=function(state){
		e.modal("hide");
		_options.closed(state);
	};
	
	e.find(".modal-body iframe").bind("load",function(){
		this.contentWindow.closeMe=closeMe;
		$(this.contentWindow.document).find(".btn[data-role=close]").bind('click',function(){
			var value = $(this).attr("return-value");
			var dataFormat = $(this).attr("return-type");
			if(dataFormat=="json"){
				value = $.parseJSON(value);
			}
			if(value)
			{
				closeMe(value);
			}
			else{
				closeMe();
			}
		});
		
		_options.load(this.contentWindow);
	});
	
	
	
	return e;
}

