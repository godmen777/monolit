var body;

(function ($) {
    $(document).ready(function () {
        'use strict';
        $(document).ajaxStart($.blockUI).ajaxStop($.unblockUI);

        body = $('body');

        body.on('submit', '.formCalc', function(){
            var form = $(this);
            var resultPrice = 0;

            $('input:not(.calcSum--input)', form).each(function (e) {
                var go = true;

                if($(this).attr("type") == "radio" || $(this).attr("type") == "checkbox") {
                    if(!$(this).prop("checked")) {
                        go = false;
                    }
                }
                else {
                    if($(this).val() == "" && $(this).data('price') != undefined) {
                        go = false;
                    }
                }


                if(go) {
                    var price = parseInt($(this).data('price'));
                    if($(this).data('multiply') != undefined && $(this).data('multiply')) {
                        price = price*parseInt($(this).val());
                    }
					
                    resultPrice = resultPrice+price;

                    
                    
                }

            });

            $('select', form).each(function (e) {
                var option = $(this).find("option:selected");
                if(option.size() > 0 && option.data('price') != undefined){
                    var price = parseInt(option.data('price'));
                    if(option.data('multiply') != undefined && option.data('multiply')) {
                        if($(this).val() != "") price = price*parseInt($(this).val());
                    }

                    resultPrice = resultPrice+price;
                }

            });
            
			resultPrice = resultPrice*parseInt($('.square_all').val());
			
            // $('.calcSumBlock').show();
            $('.b-form-calculator__price').text(resultPrice);
            $('.calcSum--input').val(resultPrice);

            return false;
        });
		
        var repairTypeSelected = false;
        $('.formCalc .repair-type input').on('change', function() {
            if($('.formCalc .square_all').val() != "") {
                 $('.formCalc').submit();
            }
            repairTypeSelected = true;    
        });
        $('.formCalc .square_all').on('keydown keyup', function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
            (e.keyCode === 65 && (e.ctrlKey === true || e.metaKey === true)) || 
            (e.keyCode >= 35 && e.keyCode <= 40)) {
                 return;
        }
        
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
        if(repairTypeSelected && e.type === "keyup") {
            $('.formCalc').submit();
        }
    });
		
    });
})(jQuery);



