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

$.getJSON("{{ site.baseurl }}/public/data/messagesByChannel.json", function (datas){
    updated = datas['updated']

    labels = datas['labels'];

    var ctx = document.getElementById('byChannel').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: datas['messagesByChannel'],
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

    var ctx2 = document.getElementById('byTsunamy').getContext('2d');
    var chart2 = new Chart(ctx2, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: datas['messagesByTsunamy'],
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

    var ctx3 = document.getElementById('usersByChannel').getContext('2d');
    var chart3 = new Chart(ctx3, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: datas['usersByChannel'],
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