function submitSearch(){
    console.log("hello")
    let search_term = $("#search_entry").val().trim()
    console.log("Searchedfor", search_term)
    let length = search_term.length
    if(length > 0){
        search_term_newpg(search_term)
    }
}

function search_term_newpg(search_term){
    window.location.replace("/search/" + search_term)
}

$(document).ready(function(){

    const data1 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Messages',
          data: [parseInt(player_data["chat_msg"]), parseInt(total["messages"])],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)'
          ],
          hoverOffset: 4
        }]
      };

      let newentry = $("<p class='text-center padded'>Your score is " + 
            parseInt(player_data["chat_msg"])
            + "</p>");
        $("#chatnum").append(newentry)

      const data2 = {
        labels: [
          'You',
          'The Mean',
        ],
        datasets: [{
            type: 'bar',
          label: 'Messages',
          data: [parseInt(player_data["messages_rank"]), parseInt(total["messages_rank"])],
          backgroundColor: [
            'rgb(54, 162, 235)'
          ],
          borderColor: [
            'rgb(54, 162, 235)'
          ],
          hoverOffset: 4
        }]
      };

    newentry = $("<p class='text-center padded'>You sent a message " + 
            (parseInt(player_data["messages_rank"]) / parseInt(total["messages_rank"])) * 100
            + "% as much as the mean</p>")
        $("#msgrank").append(newentry)

      const data3 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Wax',
          data: [parseInt(player_data["wax_number"]), parseInt(total["wax_number"])],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      }; 

      newentry = $("<p class='text-center padded'>Your score is " + 
            parseInt(player_data["got_wax"])
            + "</p>");
        $("#waxnum").append(newentry)

      const data4 = {
        labels: [
          'You',
          'The Mean',
        ],
        datasets: [{
          label: 'Ping',
          type: 'bar',
          data: [parseInt(player_data["wax_rank"]), parseInt(total["wax_rank"])],
          backgroundColor: [
            'rgb(255, 205, 86)'
          ],
          borderColor: [
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      }; 

      newentry = $("<p class='text-center padded'>You got wax " + 
            (parseInt(player_data["wax_rank"]) / parseInt(total["wax_rank"])) * 100
            + "% as much as the mean</p>")
        $("#waxrank").append(newentry)
        console.log(player_data["wax_rank"])

      const data5 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Ping',
          data: [parseInt(player_data["holding_hands_number"]), parseInt(total["holding_hands_number"])],
          backgroundColor: [
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)'
          ],
          hoverOffset: 4
        }]
      }; 

      newentry = $("<p class='text-center padded'>Your score is " + 
            parseInt(player_data["hand_held"])
            + "</p>");
        $("#handnum").append(newentry)

      const data6 = {
        labels: [
          'You',
          'The Mean',
        ],
        datasets: [{
            type: 'bar',
          label: 'Ping',
          data: [parseInt(player_data["holding_hands_rank"]), parseInt(total["holding_hands_rank"])],
          backgroundColor: [
            'rgb(54, 162, 235)'
          ],
          borderColor: [
            'rgb(54, 162, 235)'
          ],
          hoverOffset: 4
        }]
      }; 

      newentry = $("<p class='text-center padded'>You  " + 
            parseInt(player_data["holding_hands_rank"]) / parseInt(total["holding_hands_rank"]) * 100
            + "% as much as the mean</p>");
        $("#handrank").append(newentry)

        const data7 = {
            labels: [
              'You',
              'The World',
            ],
            datasets: [{
              label: 'Ping',
              data: [parseInt(player_data["ping_number"]), parseInt(total["ping_number"])],
              backgroundColor: [
                'rgb(160,32,240)',
                'rgb(119,136,153)'
              ],
              hoverOffset: 4
            }]
          }; 

          const data8 = {
            labels: [
              'You',
              'The Mean',
            ],
            datasets: [{
              label: 'Ping',
              type: 'bar',
              data: [parseInt(player_data["ping_rank"]), parseInt(total["ping_rank"])],
              backgroundColor: [
                'rgb(119,136,153)'
              ],
              borderColor: [
                'rgb(119,136,153)'
              ],
              hoverOffset: 4
            }]
          }; 

          newentry = $("<p class='text-center padded'>You pinged " + 
            parseInt(player_data["ping_rank"]) / parseInt(total["ping_rank"]) * 100
            + "% as much as the mean</p>");
        $("#pingrank").append(newentry)

      const config1 = {
        type: 'doughnut',
        data: data1,
        radius: "10%"
      };

      const config2 = {
        type: 'scatter',
        data: data2,
        options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
      };

      const config3 = {
        type: 'doughnut',
        data: data3,
        radius: "10%"
      };

      const config4 = {
        type: 'scatter',
        data: data4,
        options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
      };

      const config5 = {
        type: 'doughnut',
        data: data5,
        radius: "10%"
      };

      const config6 = {
        type: 'scatter',
        data: data6,
        options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
      };

      const config7 = {
        type: 'doughnut',
        data: data7,
        radius: "10%"
      };

      const config8 = {
        type: 'scatter',
        data: data8,
        options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
      };

  const messageNumChart = new Chart(
    document.getElementById('MessageNumChart'),
    config1
  );

  const messageRankChart = new Chart(
    document.getElementById('MessageRankChart'),
    config2
  );

  const pingNumChart = new Chart(
    document.getElementById('PingNumChart'),
    config7
  );

  const pingRankChart = new Chart(
    document.getElementById('PingRankChart'),
    config8
  );

  const handRankChart = new Chart(
    document.getElementById('HandRankChart'),
    config6
  );

  const handNumChart = new Chart(
    document.getElementById('HandNumChart'),
    config5
  );

  const waxNumChart = new Chart(
    document.getElementById('WaxNumChart'),
    config3
  );

  const waxRankChart = new Chart(
    document.getElementById('WaxRankChart'),
    config4
  );

  console.log(player_data["messages"],total["messages"])

  $( "#target" ).submit(function( event ) {
    event.preventDefault();
  });

  $("#submit_button").click(function(){
    submitSearch();
})

})