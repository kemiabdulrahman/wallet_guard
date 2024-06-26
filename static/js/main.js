$(document).ready(function() {

  const form = document.getElementById('transactionForm');
  console.log(form);

  const url = window.location.href
  console.log(url);


    // Show the transaction form when the button is clicked
    $('#showFormButton').on('click', function() {
        $('#transaction-form').removeClass('hidden');
        $('html, body').animate({
            scrollTop: $("#transaction-form").offset().top
        }, 500);
        $('#showFormButton').hide();
    });
    
    $('#transactionForm').on('submit', function(e) {
        e.preventDefault();

        const csrf = $('input[name="csrfmiddlewaretoken"]');
        const transactionType = document.getElementById('id_transaction_type');
        const amount = document.getElementById('id_amount');
        const description = document.getElementById('id_description');

        const fd = new FormData();
        fd.append('csrfmiddlewaretoken', csrf[0].value);
        fd.append('transaction_type', transactionType.value);
        fd.append('amount', amount.value);
        fd.append('description', description.value);
        

        $.ajax({
            type: "POST",
//            url: "http://localhost:8000/wallet/wallet/transaction/",
            url: `${url}transaction/`,
            data: fd,
        
            success: function(response) {
                if (response.error) {
                    alert(response.error);
                } else {
                    console.log(response);
                  $('#balance').text(response.balance);
                  $('#transaction-table tbody').prepend(
                      '<tr>' +
                          '<td><em>' + response.timestamp + '</em></td>' +
                          '<td>' + response.transaction_type + '</td>' +
                          '<td>' + response.amount + '</td>' +
                          '<td>' + response.description + '</td>' +
                      '</tr>'
                  );
                $('#transactionForm')[0].reset();
                    // Display response on a new page-like section
                    $('#response-section').html(
                        '<h2 class="fw-bold mt-3 display-5">Transaction Successful</h2>' +
                        '<p class="lead">Amount: ' + response.amount + '</p>' +
                        '<p class="lead">Type: ' + response.transaction_type + '</p>' +
                        '<p>Description: ' + response.description + '</p>' +
                        '<p>Timestamp: ' + response.timestamp + '</p>' +
                        '<button id="back-button" class="btn btn-primary btn-lg">Back</button>'
                    );
                    $('#response-section').show();
                    $('#main-content').hide();

                    // Handle back button click
                    $('#back-button').on('click', function() {
                        $('#response-section').hide();
                        $('#transaction-form').hide();
                        $('#main-content').show();
                    });
                }   
            },
            error: function(response) {
                console.log("AJAX error: ", response);
                alert('An error occurred. Please try again.');
            },
          cache: false,
          contentType: false,
          processData: false,
        });
    });
});

