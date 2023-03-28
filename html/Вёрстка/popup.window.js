
document.addEventListener('DOMContentLoaded', function() {

    var modalLoginButtons = document.querySelector('.js-open-modal-login'),
        modalSignupButtons = document.querySelector('.js-open-modal-signup'),
        overlay      = document.querySelector('#overlay-modal'),
        closeButtons = document.querySelectorAll('.js-modal-close');
    
    modalLoginButtons.addEventListener('click', function(e){
        e.preventDefault();
 
          var modalId = this.getAttribute('data-modal'),
            modalElem = document.querySelector('.modal[data-modal="' + modalId + '"]');
          
          modalElem.classList.add('active');
          overlay.classList.add('active');
    });

    modalSignupButtons.addEventListener('click', function(e){
        e.preventDefault();
 
          var modalId = this.getAttribute('data-modal'),
            modalElem = document.querySelector('.modal[data-modal="' + modalId + '"]');
          
          modalElem.classList.add('active');
          overlay.classList.add('active');
    });
    
    console.log(closeButtons);
    closeButtons.forEach(function(item) {

        item.addEventListener('click', function(e) {
            item.addEventListener('click', function(e) {
                var parentModal = this.closest('.modal');
                
                parentModal.classList.remove('active');
                overlay.classList.remove('active');
             });
        });
     
     }); // end foreach
 }); // end ready

 