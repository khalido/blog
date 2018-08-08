---
title: "SML: Deep Reinforcement Learning"
date: 2018-08-05
tags:
- meetup
---

SML's [2018-08 meetup](https://www.meetup.com/Sydney-Machine-Learning/events/252760610/).

- launching StarAI Deep Reinforcement Learning Course
  - 7 week course to take you from RL near-zero to hero
  - 10-15hrs study a week, meet 2 hrs/wk - contact paul@sydneymachinelearning.com

# [Alasdair Hamilton](https://www.linkedin.com/in/alasdair-hamilton-11852a7b/): Reinforcement learning

> The future of Artificial Intelligence is, at least partly, rooted in Reinforcement Learning. During our presentation, the team from Remi AI will take attendees on a journey through their experiences in Reinforcement Learning. Special attention will be paid to the areas in which the team have been able to apply Reinforcement Learning in a commercial setting and the four mammalian methods of learning, and how they inspire us. Remi AI has applied RL to budget and bid management, to dynamic pricing and web design, to large scale management of power requirements, inventory management, predictive maintenance. The talk will conclude with a discussion on future applications, as well as a roadmap for those looking to start out in the space, then Q&A.

- founder of [Remi AI]9https://www.linkedin.com/company/remi-pty-ltd/), one of Sydney's only RL companies
- Remi AI was founded 5 yrs ago, works on applied AI for companies/biz/ngo's.
- RL is a form of AI that includes motivating the agent toward some goal
- current RL agents are incredibly dumb - even though they excel at certain tasks
- Why RL
- its been a very long time since humans invented tools - RL is the framework which enables an artificial agent to invent more tools to solve a problem
- RL is the framework which humans use internally to learn
- RL covers a lot of domains, from engineering to pyschology
- RL is modelled around the dopamine reward delivering system in animals/humans
- some real world RL applications: stunt flight, traffic optimisation, Go (see Deepmind), dynamic pricing
- the RL agent can change its environment with its own actions. there is no supervisor, ony a reward mechanism.
- unlike supervised methods, feedbck is often delayed, so time is extremely operated. e.g in a traffic optimsation problem traffic jams can arise a lot later.
- Demo of a RL agent learning breakout
- remote control helicopter
- reward hacking - designers can set wrong or low rewards and punishments - e.g if the punishment for crashing is to high, the best stratgey is to never take off.
- space invadors
- RL in robotics is changing the field - what took decades to learn incrementally, RL systems are learning insanely quickly
- rewarding an agent: a reward is a scalar feedback signal - we dictate through rewards how well the agent is doing at step t. the best systems combine prediction and reward.
- games are a very useful way to researh RL, as you have clear scores which can be tied to rewards.
- RL is a lot harder in the real world in terms of choosing rewards and punishement.
- imitating human reward systems can be both useful and incredibly dangerous
- theres quite a range of RL algos but one powerful approach
- RL needs a huge amount of training time - agents initially know nothing so there is a huge amount of trial and error - ideally in simulation since doing this in the real world is very expensive
- a lot of RL is building a simulator to train an agent, then taking it to the real world
- todo: research transfer learning in RL
- research happening in hierarchical learning - break up things so learn individual goals which build to the final goal

- Some real world applicatoins:
  - a few cities have implemented deep RL algos in traffic optimisation. RL is also useful for devising plans on how to handle breakdowns, like a road out of commision.
  - energy reduction
  - supply chain optimisation
- RL models are simulation agnostic, but transition from simulation to the real world can be extremely troublesome
  - continually review simulators
  - where are the reward predictions going wrong

# [Alex Long](https://www.linkedin.com/in/alex-long-rl/): Deep Reinforcement Learning (Deep-RL)

> Deep Reinforcement Learning (Deep-RL) is the combination of traditional RL algorithms with the high-dimensional function approximation methods of deep learning. This combination allows Deep-RL to eclipse human performance on systems of previously intractable state-spaces and high branching factors, such as the game of GO, Atari arcade games, and heads up limit poker. In this talk I will focus on the intuition behind Deep-RL, how it compares (and differs) to other machine learning methods, as well as discuss some potential commercial applications.