$(function() {
	"use strict";
	var a = {
		series: [25, 65, 10, 14],
		chart: {
			height: 240,
			type: "donut"
		},
		legend: {
			position: "bottom",
			show: !1
		},
		plotOptions: {
			pie: {
				donut: {
					size: "80%"
				}
			}
		},
		colors: ["#17a00e", "#0d6efd", "#f41127", "#ffc107"],
		dataLabels: {
			enabled: !1
		},
		labels: ["Kids", "Men", "Women", "Furniture"],
		responsive: [{
			breakpoint: 480,
			options: {
				chart: {
					height: 200
				},
				legend: {
					position: "bottom"
				}
			}
		}]
	};
	new ApexCharts(document.querySelector("#chart15"), a).render();
});