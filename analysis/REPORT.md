# FJSP Algorithms Report

## Problem
Flexible Job Shop Scheduling assigns every operation to one eligible machine while respecting job precedence and machine non-overlap. The objective is minimum makespan.

## Generator
A seeded random generator controls machine flexibility, processing-time range and variance, and bottleneck probability. A bounded Gaussian distribution gives controllable processing-time variability. A selected bottleneck machine can be forced into eligible sets.

## Validator
The validator independently checks IDs, completeness, duplicate operations, eligible-machine assignment, non-negative time, exact completion time, job precedence and machine non-overlap.

## Algorithm
The baseline schedules operations in job order and chooses the eligible machine giving the earliest feasible completion. It is a transparent heuristic, not an exact optimizer.

## Experiments and failure analysis
Experiments use multiple seeds and named instance classes. High flexibility increases assignment choices and can make local greedy decisions harmful downstream. Bottleneck-heavy instances expose contention because many operations compete for the same machine. High processing-time variance can also make locally attractive choices globally poor.

## Improvements
Congestion-aware selection, look-ahead, local search, and lower-bound gap reporting are natural next steps.

## Reproducibility
Every generated instance stores its seed and generator parameters.
