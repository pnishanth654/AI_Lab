% Facts: Define family relationships
parent(john, jim).
parent(john, sara).
parent(jane, jim).
parent(jane, sara).
parent(bob, john).
parent(bob, lisa).
parent(lisa, ann).

% Rules: Define additional relationships using facts
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.  % X and Y are not the same person

% Sample Queries:
% parent(jane, Child).
% sibling(jim, Sibling).
% grandparent(Grandparent, ann).