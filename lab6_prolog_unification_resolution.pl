% UNIFICATION

unify(X, X) :- var(X), !.
unify(X, Y) :- var(X), !, X = Y.
unify(X, Y) :- var(Y), !, Y = X.
unify(X, Y) :- compound(X), compound(Y), !,
               X =.. [F|Xs], Y =.. [F|Ys],
               unify_list(Xs, Ys).

unify_list([], []).
unify_list([X|Xs], [Y|Ys]) :- unify(X, Y), unify_list(Xs, Ys).

% RESOLUTION

resolution(Goal, Clauses) :-
    member(Clause, Clauses),
    resolve(Goal, Clause, Resolvent),
    (member([], Resolvent) ->
        writeln('Goal is true.');
        resolution(Resolvent, Clauses)
    ).

resolve(Goal, Clause, Resolvent) :-
    select(Literal, Goal, RestGoal),
    select(not(Literal), Clause, RestClause),
    append(RestGoal, RestClause, Resolvent).