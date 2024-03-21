# ABM Simulations: Game: Rock-Paper-Scissor-Lizard-Spock

## Application Domain of the Simulation:

**educational training**: ABM, Game Theory: It serves as a practical introduction to game theory, demonstrating how different strategies can result in varied outcomes and how to anticipate and counter opponents' moves.

**behaviour economics**: The game's dynamics and strategies can be applied to study behavioral economics, specifically how individuals make decisions in uncertain conditions and how they value risk and reward. This can lead to insights into economic decision-making, market strategies, and negotiation tactics.

**reinforcement learning**: The game can be a testbed for reinforcement learning models, where AI agents learn optimal strategies through repeated play and adaptation. Insights gained can contribute to the development of more sophisticated AI systems capable of learning and evolving strategies in dynamic environments.

## Game Design

#### Objective
Players aim to play 1000 rounds through strategic selection of gestures (Rock, Paper, Scissors, Lizard, Spock), 
each with its own payoff, and see which player has more points. 

#### Payoff Rules

- Rock defeats Scissors and Lizard; +3 for a win, -3 for a loss
- Paper defeats Rock and Spock; +2 for a win, -2 for a loss
- Scissors defeats Paper and Lizard; +1 for a win, -1 for a loss
- Lizard defeats Spock and Paper; +4 for a win, -4 for a loss
- Spock defeats Scissors and Rock; +5 for a win, -5 for a loss

## Strategies


## Files:

1. For ABM_Project_V4, the code for adaptive strategy doesn't look correct. There shouldn't be 
obvious winning rate pattern as the simulations increase. 


2. For RPSLS, it contains proper code for each strategy, and has some nice visualization. 

## References

1. Gu, S. (2013). From Rock Scissor Paper to study and modeling of Chinese Five Elements: Evolutionary Game Theory. In 75. https://brage.bibsys.no/xmlui/handle/11250/247175

2. Xu, B., & Wang, Z. (2012). Asymmetry Spectrum of cycle amplitude in Rock-Paper-Scissor Game of Experimental Economics. Social Science Research Network. https://doi.org/10.2139/ssrn.2085459

3. Kang, Y., Pan, Q., Wang, X., & He, M. (2013). A golden point rule in rock–paper–scissors–lizard–spock game. Physica A: Statistical Mechanics and Its Applications, 392(11), 2652–2659. https://doi.org/10.1016/j.physa.2012.10.011

4. Vukov, J., Szolnoki, A., & Szabó, G. (2013). Diverging fluctuations in a spatial five-species cyclic dominance game. Physical Review E, 88(2). https://doi.org/10.1103/physreve.88.022123