
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
	e.on('hidden.bs.modal', function (e) {
		  // do something...
		_options.closed($(e.target).data("state"));
	});	
	var closeMe=function(state){
		e.data("state",state);
		e.modal("hide");
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


function showMessage(options){
	var _options={
			width:320,
			height:240,			
			"title":"消息框",
			"body":"",
			"buttons":[{"id":"btnOK","text":"确定"}],
			"defaultButton":"btnOK",
			closed:function(state){}
	};
	if(typeof(options)=="string"){
		_options["body"]=options;
	}
	else if(typeof(options)=="object"){
		$.extend(_options,options);
	}
	
	var html = '<div class="modal fade" id="__dialog__" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">'
	  +'<div class="modal-dialog" role="document">'
	    +'<div class="modal-content">'
	      +'<div class="modal-header">'
            +'<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>'
        	+'<h4 class="modal-title">Modal title</h4>'
          +'</div>'
	      +'<div class="modal-body">'
	      +'</div>'
	      +'<div class="modal-footer">'
	      +'</div>'
	    +'</div>'
	  +'</div>'
	+'</div>';
	var e = window.top.$(html);
	e.find(".modal-dialog").width(_options.width);
	e.find(".modal-body iframe").height(_options.height);
	
	if(typeof(_options["body"])=="string"){
		e.find(".modal-body").html(_options["body"]);
	}
	else if(typeof(_option["body"])=="object"){
		e.find(".modal-body").append(_options["body"]);
	}
	e.find(".modal-title").html(_options["title"]);
	
	e.modal("show");
	
	var closeMe=function(state){
		//e.data("state",state);
		_options["result"]=state;
		e.modal("hide");
	};
	e.on('hidden.bs.modal', function (e) {
		  // do something...
		_options.closed(_options["result"]);
	});
	var footer=$(e).find(".modal-footer");
	
	for(var i in _options.buttons){
		var opt = _options.buttons[i];
		var btn=$("<button class='btn'>");
		btn.attr("data-role",opt["id"]);
		btn.append($("<span class='text'>"+opt["text"]+"</span>"));
		btn.click(function(){
			closeMe($(this).attr("data-role"));
		});
		if(opt["id"]==_options["defaultButton"]){
			btn.addClass("btn-primary");
		}
		else{
			btn.addClass("btn-default");
		}
		footer.append(btn);
	}
	e.modal('show');
	return e;
}
