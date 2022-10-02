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
          data: [parseInt(player_data["messages"]), parseInt(total["messages"])],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)'
          ],
          hoverOffset: 4
        }]
      };

      const data2 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Messages',
          data: [parseInt(player_data["messages_rank"]), parseInt(total["messages_rank"])],
          backgroundColor: [
            'rgb(54, 162, 235)',
            'rgb(255, 99, 132)'
          ],
          hoverOffset: 4
        }]
      };

      let newentry = $("<p class='text-center padded'>You are in the top " + 
            (parseInt(player_data["messages_rank"]) / parseInt(total["messages_rank"])) * 100
            + "% of users</p>")
        $("#msgrank").append(newentry)

      const data3 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Ping',
          data: [parseInt(player_data["ping_number"]), parseInt(total["ping_number"])],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      }; 

      const data4 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Ping',
          data: [parseInt(player_data["ping_rank"]), parseInt(total["ping_rank"])],
          backgroundColor: [
            'rgb(255, 205, 86)',
            'rgb(255, 99, 132)'
          ],
          hoverOffset: 4
        }]
      }; 

      newentry = $("<p class='text-center padded'>You are in the top " + 
            (parseInt(player_data["ping_rank"]) / parseInt(total["ping_rank"])) * 100
            + "% of users</p>")
        $("#pingrank").append(newentry)

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

      const data6 = {
        labels: [
          'You',
          'The World',
        ],
        datasets: [{
          label: 'Ping',
          data: [parseInt(player_data["holding_hands_rank"]), parseInt(total["holding_hands_rank"])],
          backgroundColor: [
            'rgb(54, 162, 235)',
            'rgb(75, 192, 192)'
          ],
          hoverOffset: 4
        }]
      }; 

      newentry = $("<p class='text-center padded'>You are in the top " + 
            (parseInt(player_data["holding_hands_rank"]) / parseInt(total["holding_hands_rank"])) * 100
            + "% of users</p>")
        $("#handrank").append(newentry)

      const config1 = {
        type: 'doughnut',
        data: data1,
        radius: "10%"
      };

      const config2 = {
        type: 'doughnut',
        data: data2,
        radius: "10%"
      };

      const config3 = {
        type: 'doughnut',
        data: data3,
        radius: "10%"
      };

      const config4 = {
        type: 'doughnut',
        data: data4,
        radius: "10%"
      };

      const config5 = {
        type: 'doughnut',
        data: data5,
        radius: "10%"
      };

      const config6 = {
        type: 'doughnut',
        data: data6,
        radius: "10%"
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
    config3
  );

  const pingRankChart = new Chart(
    document.getElementById('PingRankChart'),
    config4
  );

  const handRankChart = new Chart(
    document.getElementById('HandRankChart'),
    config6
  );

  const handNumChart = new Chart(
    document.getElementById('HandNumChart'),
    config5
  );

  console.log(player_data["messages"],total["messages"])

  $( "#target" ).submit(function( event ) {
    event.preventDefault();
  });

  $("#submit_button").click(function(){
    submitSearch();
})

})