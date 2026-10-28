/*  all_diff:   all the values in the given list should be different  */

all_diff([]).
all_diff([H|T]) :- \+ member(H,T), all_diff(T).

/* X is numerically to the left of Y, i.e, X is smaller than Y */

left_of(X,Y) :- X < Y.

/* X is numerically to the immediate left of Y */

immediate_left_of(X,Y) :- Y - X =:= 1.

/* X is numerically not adjacent of Y */

not_adjacent(X,Y):- X < Y, Y - X > 1.
not_adjacent(X,Y) :- X > Y, X - Y > 1.

houses([A, B, C, D]) :- 
    member(A, [1,2,3,4]), 
    member(B, [1,2,3,4]),
    member(C, [1,2,3]),
    member(D, [1,3,4]),

    all_diff([A,B,C,D]),
    immediate_left_of(A,B),
    left_of(D,B),
    not_adjacent(B,C)
