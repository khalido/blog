---
title: "SML 2018-08: Deep Reinforcement Learning"
description: "notes from the meetup"
category: [meetup, data science]
layout: post
toc: true
---

SML's [2018-08 meetup](https://www.meetup.com/Sydney-Machine-Learning/events/252760610/).

- launching StarAI Deep Reinforcement Learning Course
  - 7 week course to take you from RL near-zero to hero
  - 10-15hrs study a week, meet 6-8pm once a week

the talks:

# [Alasdair Hamilton](https://www.linkedin.com/in/alasdair-hamilton-11852a7b/): Reinforcement learning

> The future of Artificial Intelligence is, at least partly, rooted in Reinforcement Learning. During our presentation, the team from Remi AI will take attendees on a journey through their experiences in Reinforcement Learning. Special attention will be paid to the areas in which the team have been able to apply Reinforcement Learning in a commercial setting and the four mammalian methods of learning, and how they inspire us. Remi AI has applied RL to budget and bid management, to dynamic pricing and web design, to large scale management of power requirements, inventory management, predictive maintenance. The talk will conclude with a discussion on future applications, as well as a roadmap for those looking to start out in the space, then Q&A.

- founder of [Remi AI](https://www.linkedin.com/company/remi-pty-ltd/), one of Sydney's only RL companies.
- Remi AI was founded 5 yrs ago, works on applied AI for companies/biz/ngo's.
- RL is a form of AI that includes motivating the agent toward some goal.
- current RL agents are incredibly dumb - even though they excel at certain tasks.
- Why RL:
  - its been a very long time since humans invented tools - RL is the framework which enables an artificial agent to invent more tools to solve a problem
  - RL is the framework which humans use internally to learn
  - RL covers a lot of domains, from engineering to pyschology
  - RL is modelled around the dopamine reward delivering system in animals/humans
- some real world RL applications: stunt flight, traffic optimisation, Go (see Deepmind), dynamic pricing
- the RL agent can change its environment with its own actions. there is no supervisor, ony a reward mechanism.
- unlike supervised methods, feedbck is often delayed, so time is extremely important. e.g in a traffic optimsation problem traffic jams can arise a long time after a decision.
- Demoed of a RL agent learning breakout, a remote control helicopter and space invadors.
- reward hacking - designers can set wrong or low rewards and punishments - e.g if the punishment for crashing is to high, the best stratgey is to never take off.
- RL in robotics is changing the field - what took decades to learn incrementally, RL systems are learning insanely quickly.
- rewarding an agent: a reward is a scalar feedback signal - we dictate through rewards how well the agent is doing at step t. the best systems combine prediction and reward.
- games are a very useful way to researh RL, as you have clear scores which can be tied to rewards and punishments.
- RL is a lot harder in the real world in terms of choosing rewards and punishement.
- imitating human reward systems can be both useful and incredibly dangerous.
- there is quite a range of RL algos.
- RL needs a huge amount of training time - agents initially know nothing so there is a lot of trial and error - ideally in simulation since doing this in the real world is very expensive
- a lot of RL is building a simulator to train an agent, then taking it to the real world.
- todo: research transfer learning in RL.
- research happening in hierarchical learning - break up things so learn individual goals which build to the final goal.
- Some real world applications of RL:
  - a few cities have implemented deep RL algos in traffic optimisation. RL is also useful for devising plans on how to handle breakdowns, like a road out of commision.
  - energy reduction - [Google's data center](https://deepmind.com/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-40/)
  - supply chain optimisation - warehousing, logistic.
- RL models are simulation agnostic, but transition from simulation to the real world can be extremely troublesome. So:
  - continually review simulators.
  - where are the reward predictions going wrong?

q & a

- How do you reward differnt/multiple objectives?
  - for a wide range of objectives, scale up rewards at different levels - example reward individual contract signings and also bigger level revenue goals.
- is RL limited by the complexity of the simulation?
  - some things can be simulated by very simple things like graphs written in python - sims don't have to be complex and visual.
- arbitary rewards can cause problems - whats a good fix?
  - its a hot area - ppl are figuring out best utility functions for rewards.


# [Alex Long](https://www.linkedin.com/in/alex-long-rl/): Deep Reinforcement Learning: Zero to PPO in 20 minutes

> Deep Reinforcement Learning (Deep-RL) is the combination of traditional RL algorithms with the high-dimensional function approximation methods of deep learning. This combination allows Deep-RL to eclipse human performance on systems of previously intractable state-spaces and high branching factors, such as the game of GO, Atari arcade games, and heads up limit poker. In this talk I will focus on the intuition behind Deep-RL, how it compares (and differs) to other machine learning methods, as well as discuss some potential commercial applications.

- goal is to wow the audience with how general Proximal Policy Optimization (PPO) is.
- OpenAI used PPO to learn DOTA and beat professionals, exact same algo can be used to learn/do totally something else.
- context: where does RL fit?
- general RL: I'm in situation X and my overall goal is y. What do I need to do?
- RL is very general, fits with and takes bits of all parts of AI.
- see [ben recht's blog](http://www.argmin.net/) on RL.
- a way to think of any move choosing machine is as a tuneable black box which looks at the state of the world and spits out a probablity for all possible moves.
- RL is adjusting this move choosing machine so that the likelihood of good moves is higher and bad moves lower. Thats it. Of course, you need to do this many times over.
- one move choosing machines can be a NN, which are nice since they let us generalize inputs we haven't seen before by learning the underlying data distribution.
- the simplest way of recording moves is just making a table of moves and a score, but this doesn't help us with moves we haven't seen. A naive answer is to pick the closest neighbours, or interpolate linearly. Neural networks allow us to approximate the underlying distribution, which allows us to reason about states we haven't seen before.
- how do we train our NN to approximate a game globally when we are using the NN itself to collect the data we are using for training?
  - be extremely careful about how we explore the space
  - be extremely carefeul about how we update our NN
- Policy gradients gives us a safe way to update the NN, but have lots of issues
- Proximal Policy Optimization uses a surrogate loss.
- key diff: using the ratio of probabilites b/w old and new policies and limit the amount this can be updated. This bounds policy updates and introduces stability.
- the engineering behind RL algos is impresisve and important - the algorithims can be straightforward but see all the engineering/computing resources OpenAI is throwing at their RL algos playing computer games like DOTA.

q & a

- problem of local minima?
  - in a multi-dimensional world, the local minima generally disappear, as there are so many directions to move. It does exist, but in a different way from SL.
  - there is a problem of getting stuck in a bad policy space so never learning 'good' moves.
- what about overfitting?
  - we can't overfit - there is no test set. We're doing RL in an environment where we want it to win the mostest.
- how many policies do u keep track of?
  - only two - current and one step ahead
- is there a q value in PPO?
  - in policy gradient methods you don't have a q
- catostrophic policy updates - how often do u have to abondon?
  - vanilla policy gradients, have to restart all the time, then tune hyperparameters.
  - PPO almost never, it generally figures things out.
- how efficient is RL?
  - RL uses huge amounts of compute but is progressing very fast, in orders of magnitude. At the moment its prohibitvely expensive for normal ppl to train things like DOTA bots but it keeps getting computationaly cheaper as algos improve.
