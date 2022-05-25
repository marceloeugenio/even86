$(function() {
	"use strict";
	var e = {
		series: [{
			name: "Inscrições",
			data: [427, 613, 801, 457, 605, 414, 671, 360, 540, 34, 12]
		}],
		chart: {
			foreColor: "#6c757d",
			type: "bar",
			height: 390,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 12,
				blur: 3,
				opacity: .1,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !1
			}
		},
		plotOptions: {
			radialBar: {
				hollow: {
					size: "70%"
				}
			},
			bar: {
				horizontal: !1,
				columnWidth: "35%",
				endingShape: "rounded"
			}
		},
		markers: {
			size: 0,
			colors: ["#0d6efd"],
			strokeColors: "#fff",
			strokeWidth: 2,
			hover: {
				size: 7
			}
		},
		dataLabels: {
			enabled: !1
		},
		stroke: {
			show: !0,
			width: 3,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Nov", "Dez"]
		},
		fill: {
			opacity: 1
		}
	};
	new ApexCharts(document.querySelector("#chart21"), e).render()
});