% Step 1: Define Facts and Rules
is_a(dog, mammal).
is_a(mammal, animal).
is_a(cat, mammal).

% Rules
is_a(X, animal) :- is_a(X, mammal).
is_a(X, mammal) :- is_a(X, dog).

% Step 2: Define Backward Chaining Predicate
backward_chain(Goal) :-
    is_a(Goal, _).
backward_chain(Goal) :-
    is_a(Intermediate, Goal),
    backward_chain(Intermediate).

% Example Query:
% backward_chain(is_a(cat, animal)).