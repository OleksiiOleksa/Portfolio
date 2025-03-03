$(function() {

    /* Filter ==============*/ 
    let filter = $("[data-filter]");

    filter.on("click", function(event) {
        event.preventDefault();

        let cat = $(this).data('filter');

        if (cat == 'all') {
            $("[data-cat]").removeClass("hide");
        } else {
            $("[data-cat]").each(function() {

                let workCat = $(this).data('cat');

                if (workCat != cat) {
                    $(this).addClass('hide');
                } else {
                    $(this).removeClass('hide');
                }

            });
        }
    });

    /* Modal ==============*/

    const modalCall = $("[data-modal]"); 
    const modalClose = $("[data-close]"); 
    
    
    modalCall.on("click", function(event) {
        event.preventDefault(); 

        let modalId = $(this).data('modal'); 
        console.log("Opening modal:", modalId); 

        $(modalId).addClass('show'); 
        $("body").addClass('no-scroll'); 
    });

    
    modalClose.on("click", function(event) {
        event.preventDefault(); 

        let modalParent = $(this).closest('.modal'); 
        console.log("Closing modal:", modalParent); 

        modalParent.removeClass('show'); 
        $("body").removeClass('no-scroll'); 
    });

     
     if ($('.messages').length) {
        
        setTimeout(function() {
            const messages = document.querySelector('.messages'); 
            if (messages) {
                messages.style.transition = "opacity 0.5s"; 
                messages.style.opacity = "0"; 
                setTimeout(() => messages.remove(), 500); 
            }
        }, 3000); 
    }

});
