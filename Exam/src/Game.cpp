#pragma once
#include <string>
#include <iostream>
#include <SFML/Graphics.hpp>
#include <Ball.hpp>
#include <Game.hpp>

namespace mt {
	Game::~Game() {
		if (m_window != nullptr)
			delete m_window;
	}

	void Game::SetCaption(const std::string& caption) {
		m_caption = caption;
	}

	void Game::SetResolution(int width, int height) {
		m_width = width;
		m_height = height;
	}

	void Game::Setup() {
		m_window = new sf::RenderWindow(sf::VideoMode(m_width, m_height), m_caption);
	}

	void Game::Wall(mt::Ball* ball) {
		//mt::Ball ball = *ball1;
		Point p = (*ball).GetPosition();
		float r = (*ball).Radius();
		Vec v = (*ball).GetVelocity();

		if (p.y + r > m_height && v.y > 0)
			(*ball).SetVelocity({ v.x, -v.y });

		if (p.y - r < 0 && v.y < 0)
			(*ball).SetVelocity({ v.x, -v.y });

		if (p.x + r >= m_width && v.x > 0)
			(*ball).SetVelocity({ -v.x, v.y });

		if (p.x - r <= 0 && v.x < 0)
			(*ball).SetVelocity({ -v.x, v.y });

	}

	void Game::Run() {
		/*
		std::vector<mt::Ball*> balls;

		balls.emplace_back(new mt::Ball({ 0,0 }, 50, sf::Color::Red));
		balls.emplace_back(new mt::Ball({ 0,300 }, 30, sf::Color::Yellow));

		balls[0]->SetVelocity({ 100,150 });
		balls[1]->SetVelocity({ 80,80 });
		*/

		mt::Ball ball({ 50,100 }, 50, sf::Color::Blue);
		ball.SetVelocity({ 1000,1000 });

		sf::Clock timer;

		while (m_window->isOpen()) {
			sf::Event event;
			while (m_window->pollEvent(event)) {
				if (event.type == sf::Event::Closed)
					m_window->close();
			}

			sf::Time dt = timer.restart();
			//std::cout << dt.asSeconds() << balls[1]->GetPosition().x << " " << balls[1]->GetPosition().y << std::endl

			ball.Move(dt.asSeconds());

			Wall(&ball);

			//ball.Move(dt.asSeconds());

			m_window->clear();

			m_window->draw(*ball.Get());
			m_window->display();
		}

		//for (int i = 0; i < balls.size(); i++)
		//	delete balls[i];

	}
}
