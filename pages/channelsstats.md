---
layout: page
permalink: /channelsstats/
title: Statistiques du Chat
linktitle: "Statistiques du Chat"
linkurl: /channelsstats/
description: "Statistiques sur le chat https://coa.crapaud-fou.org"
chartjs: true
jquery: true
---

Statistiques du <a href="https://coa.crapaud-fou.org">chat</a> (aussi connu sous le nom de mare aux crapauds) :
<canvas id="byChannel"></canvas>
<canvas id="byTsunamy"></canvas>
<canvas id="usersByChannel"></canvas>
<script>
updated = "updated 02/05/2019"
labels = ["mai 2018","juin 2018","juillet 2018","août 2018","septembre 2018","octobre 2018","novembre 2018","décembre 2018","janvier 2019","février 2019","mars 2019","avril 2019"];

$.getJSON("{{ site.baseurl }}/public/data/messagesByChannel.json", function (datas){
    var ctx = document.getElementById('byChannel').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: datas,
        },

        // Configuration options go here
        options: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: "Nombre de message par canaux (" + updated + ")",
                position: "top"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        stepSize: 500
                    }
                }]
            }
        }
    });
});

$.getJSON("{{ site.baseurl }}/public/data/messagesByTsunami.json", function (datas){
    var ctx2 = document.getElementById('byTsunamy').getContext('2d');
    var chart2 = new Chart(ctx2, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: datas,
        },

        // Configuration options go here
        options: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: "Nombre de message par Tsunami (" + updated + ")",
                position: "top"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        stepSize: 500
                    }
                }]
            }
        }
    });
});

$.getJSON("{{ site.baseurl }}/public/data/activeUsersByChannel.json", function (datas){
    var ctx3 = document.getElementById('usersByChannel').getContext('2d');
    var chart3 = new Chart(ctx3, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: datas,
        },

        // Configuration options go here
        options: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: "Nombre d'utilisateur actifs par canaux (" + updated + ")",
                position: "top"
            },
            responsive: true,
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        stepSize: 50
                    }
                }]
            }
        }
    });
});
</script>