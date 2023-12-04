#!/usr/bin/env python3

from ispcr import step_two

sorted_good_hits = [
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '46920', '46938', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '47211', '47192', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '144156', '144174', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '144447', '144428', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '149622', '149640', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '149913', '149894', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '401483', '401501', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '401774', '401755', '0.45', '26.1', '20'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '2321911', '2321930', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '2322202', '2322184', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '2683111', '2683130', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '2683402', '2683384', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '2688655', '2688674', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '2688946', '2688928', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '2694199', '2694218', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '2694490', '2694472', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '2771804', '2771823', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '2772095', '2772077', '0.005', '32.4', '19'],
	['806R', 'NZ_CP028827.1', '85.000', '20', '3', '0', '1', '20', '2945147', '2945166', '0.45', '26.1', '20'],
	['515F', 'NZ_CP028827.1', '89.474', '19', '2', '0', '1', '19', '2945438', '2945420', '0.005', '32.4', '19']
]

paired_hits = step_two(
	sorted_hits=sorted_good_hits,
	max_amplicon_size=1000
)

for hit in paired_hits:
	print(hit)


