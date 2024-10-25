#pragma once
#include <string>
#include <iostream>
#include <SFML/Graphics.hpp>
#include <Ball.hpp>

namespace mt {
	class Game {
	private:
		int m_width = 0;
		int m_height = 0;
		std::string m_caption;
		sf::RenderWindow* m_window = nullptr;
		//std::vector<mt::Ball*> m_balls;

	public:
		Game() {

		}
		~Game();

		void SetCaption(const std::string& caption);

		void SetResolution(int width, int height);

		void Setup();

		void Wall(mt::Ball* ball);

		void Run();
	};
}