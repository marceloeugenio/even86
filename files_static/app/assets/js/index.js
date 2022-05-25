$(function() {
	"use strict";
	var e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613, 727, 414, 555, 257]
		}],
		chart: {
			type: "line",
			height: 65,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !0,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#17a00e"
			},
			sparkline: {
				enabled: !0
			}
		},
		markers: {
			size: 0,
			colors: ["#17a00e"],
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
		colors: ["#17a00e"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart1"), e).render();
	e = {
		series: [{
			name: "Customers",
			data: [240, 160, 671, 414, 555, 257, 901, 613, 727, 414, 555, 257]
		}],
		chart: {
			type: "line",
			height: 65,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !0,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#ffc107"
			},
			sparkline: {
				enabled: !0
			}
		},
		markers: {
			size: 0,
			colors: ["#ffc107"],
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
		colors: ["#ffc107"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart2"), e).render();
	e = {
		series: [{
			name: "Store Visitores",
			data: [240, 160, 671, 414, 555, 257, 901, 613, 727, 414, 555, 257]
		}],
		chart: {
			type: "line",
			height: 65,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !0,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#f41127"
			},
			sparkline: {
				enabled: !0
			}
		},
		markers: {
			size: 0,
			colors: ["#f41127"],
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
		colors: ["#f41127"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart3"), e).render();
	e = {
		series: [{
			name: "Total Sales",
			data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
		}, {
			name: "Customers",
			data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
		}, {
			name: "Store Visitores",
			data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
		}],
		chart: {
			foreColor: "#9ba7b2",
			type: "bar",
			height: 300,
			toolbar: {
				show: !1
			}
		},
		plotOptions: {
			bar: {
				horizontal: !1,
				columnWidth: "55%",
				endingShape: "rounded"
			}
		},
		dataLabels: {
			enabled: !1
		},
		stroke: {
			show: !0,
			width: 2,
			colors: ["transparent"]
		},
		colors: ["#0dcaf0", "#0d6efd", "#e5e7e8"],
		xaxis: {
			categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			y: {
				formatter: function(e) {
					return "$ " + e + " thousands"
				}
			}
		}
	};
	new ApexCharts(document.querySelector("#chart4"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart5"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart6"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart7"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart8"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart9"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart10"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [240, 160, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 45,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !0
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0d6efd"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart11"), e).render();
	e = {
		series: [{
			name: "Revenue",
			data: [332, 540, 160, 240, 160, 671, 355, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 100,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#17a00e"
			},
			sparkline: {
				enabled: !0
			}
		},
		markers: {
			size: 0,
			colors: ["#17a00e"],
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#17a00e"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart12"), e).render();
	e = {
		series: [{
			name: "Pageviews",
			data: [332, 540, 160, 240, 160, 671, 355, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 100,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#f41127"
			},
			sparkline: {
				enabled: !0
			}
		},
		markers: {
			size: 0,
			colors: ["#f41127"],
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#f41127"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart13"), e).render();
	e = {
		series: [{
			name: "New Sessions",
			data: [332, 540, 160, 240, 160, 671, 355, 671, 414, 555, 257, 901, 613]
		}],
		chart: {
			type: "area",
			height: 100,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !1,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0dcaf0"
			},
			sparkline: {
				enabled: !0
			}
		},
		markers: {
			size: 0,
			colors: ["#0dcaf0"],
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
			width: 2,
			curve: "smooth"
		},
		colors: ["#0dcaf0"],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(e) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart14"), e).render();
	e = {
		chart: {
			height: 180,
			type: "radialBar",
			toolbar: {
				show: !1
			}
		},
		plotOptions: {
			radialBar: {
				hollow: {
					margin: 0,
					size: "78%",
					background: "#ceffca",
					image: void 0,
					imageOffsetX: 0,
					imageOffsetY: 0,
					position: "front",
					dropShadow: {
						enabled: !1,
						top: 3,
						left: 0,
						blur: 4,
						color: "rgba(0, 169, 255, 0.85)",
						opacity: .65
					}
				},
				track: {
					margin: 0,
					dropShadow: {
						enabled: !1,
						top: -3,
						left: 0,
						blur: 4,
						color: "rgba(0, 169, 255, 0.85)",
						opacity: .65
					}
				},
				dataLabels: {
					showOn: "always",
					name: {
						offsetY: -8,
						show: !0,
						color: "#6c757d",
						fontSize: "15px"
					},
					value: {
						formatter: function(e) {
							return e + "%"
						},
						color: "#000",
						fontSize: "25px",
						show: !0,
						offsetY: 10
					}
				}
			}
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "light",
				type: "horizontal",
				shadeIntensity: .5,
				gradientToColors: ["#17a00e"],
				inverseColors: !1,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 100]
			}
		},
		colors: ["#17a00e"],
		series: [68],
		stroke: {
			lineCap: "round",
			width: "5"
		},
		labels: ["Completed"]
	};
	new ApexCharts(document.querySelector("#chart16"), e).render();
	e = {
		chart: {
			height: 180,
			type: "radialBar",
			toolbar: {
				show: !1
			}
		},
		plotOptions: {
			radialBar: {
				hollow: {
					margin: 0,
					size: "78%",
					background: "#ffd6da",
					image: void 0,
					imageOffsetX: 0,
					imageOffsetY: 0,
					position: "front",
					dropShadow: {
						enabled: !1,
						top: 3,
						left: 0,
						blur: 4,
						color: "rgba(0, 169, 255, 0.85)",
						opacity: .65
					}
				},
				track: {
					margin: 0,
					dropShadow: {
						enabled: !1,
						top: -3,
						left: 0,
						blur: 4,
						color: "rgba(0, 169, 255, 0.85)",
						opacity: .65
					}
				},
				dataLabels: {
					showOn: "always",
					name: {
						offsetY: -8,
						show: !0,
						color: "#6c757d",
						fontSize: "15px"
					},
					value: {
						formatter: function(e) {
							return e + "%"
						},
						color: "#000",
						fontSize: "25px",
						show: !0,
						offsetY: 10
					}
				}
			}
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "light",
				type: "horizontal",
				shadeIntensity: .5,
				gradientToColors: ["#f41127"],
				inverseColors: !1,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 100]
			}
		},
		colors: ["#f41127"],
		series: [60],
		stroke: {
			lineCap: "round"
		},
		labels: ["Cancelled"]
	};
	new ApexCharts(document.querySelector("#chart17"), e).render();
	e = {
		chart: {
			height: 180,
			type: "radialBar",
			toolbar: {
				show: !1
			}
		},
		plotOptions: {
			radialBar: {
				hollow: {
					margin: 0,
					size: "78%",
					background: "#ffedb9",
					image: void 0,
					imageOffsetX: 0,
					imageOffsetY: 0,
					position: "front",
					dropShadow: {
						enabled: !1,
						top: 3,
						left: 0,
						blur: 4,
						color: "rgba(0, 169, 255, 0.85)",
						opacity: .65
					}
				},
				track: {
					margin: 0,
					dropShadow: {
						enabled: !1,
						top: -3,
						left: 0,
						blur: 4,
						color: "rgba(0, 169, 255, 0.85)",
						opacity: .65
					}
				},
				dataLabels: {
					showOn: "always",
					name: {
						offsetY: -8,
						show: !0,
						color: "#6c757d",
						fontSize: "15px"
					},
					value: {
						formatter: function(e) {
							return e + "%"
						},
						color: "#000",
						fontSize: "25px",
						show: !0,
						offsetY: 10
					}
				}
			}
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "light",
				type: "horizontal",
				shadeIntensity: .5,
				gradientToColors: ["#ffc107"],
				inverseColors: !1,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 100]
			}
		},
		colors: ["#ffc107"],
		series: [45],
		stroke: {
			lineCap: "round"
		},
		labels: ["In Progress"]
	};
	new ApexCharts(document.querySelector("#chart18"), e).render();
	e = {
		series: [{
			name: "Orders",
			data: [240, 160, 671, 414, 555, 257, 901, 613, 727, 414, 555, 257]
		}],
		chart: {
			foreColor: "#9ba7b2",
			type: "bar",
			height: 270,
			toolbar: {
				show: !1
			},
			zoom: {
				enabled: !1
			},
			dropShadow: {
				enabled: !0,
				top: 3,
				left: 14,
				blur: 4,
				opacity: .12,
				color: "#0d6efd"
			},
			sparkline: {
				enabled: !1
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
		plotOptions: {
			bar: {
				horizontal: !1,
				columnWidth: "30%",
				endingShape: "rounded"
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
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			theme: "dark",
			fixed: {
				enabled: !1
			},
			x: {
				show: !0
			},
			y: {
				formatter: function(e) {
					return " " + e + " "
				}
			},
			marker: {
				show: !1
			}
		}
	};
	new ApexCharts(document.querySelector("#chart19"), e).render();
	
	
	
	
	$(document).ready(function() {
		$('#Transaction-History').DataTable({
			lengthMenu: [[6, 10, 20, -1], [6, 10, 20, 'Todos']]
		});
	  } );
	  
	  
	  
	  
	    new PerfectScrollbar('.product-list');
		new PerfectScrollbar('.customers-list');
	
	
	
	
	
	
	
});