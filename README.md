# Lettepa

Lettepa is a color theme inspired by [solarized] and [gruvbox].

[gruvbox]: https://github.com/morhetz/gruvbox
[solarized]: https://github.com/altercation/solarized

## Table of contents

- [Palette](#palette)
- [Color modes](#color-modes)
  - [Dark mode](#dark-mode)
  - [Light mode](#light-mode)
- [Ports](#ports)
- [License](#license)

## Palette

Nearly half of the colors are picked from [nipponcolors], and the remaining
colors are generated with the help of [huetone].

[huetone]: https://github.com/ardov/huetone
[nipponcolors]: https://nipponcolors.com

| Color                                | Name          | Hex       | OKLCH                        | XTerm Number (Approx.) |
| ------------------------------------ | ------------- | --------- | ---------------------------- | ---------------------- |
| ![Kurenai](assets/Kurenai.svg)       | [Kurenai]     | `#CB1B45` | `oklch(54.41% 0.205 16.02)`  | 100                    |
| ![Nakabeni](assets/Nakabeni.svg)     | [Nakabeni]    | `#ED5A65` | `oklch(66.26% 0.181 19.18)`  | 167                    |
| ![Aomidori](assets/Aomidori.svg)     | [Aomidori]    | `#00AA90` | `oklch(65.96% 0.123 176.57)` | 36                     |
| ![brAomidori](assets/brAomidori.svg) | brAomidori    | `#47D2BC` | `oklch(78.39% 0.122 180.32)` | 79                     |
| ![Ruri](assets/Ruri.svg)             | [Ruri]        | `#005CAF` | `oklch(47.8% 0.151 253.85)`  | 25                     |
| ![brRuri](assets/brRuri.svg)         | brRuri        | `#37B4FD` | `oklch(73.52% 0.149 239.83)` | 39                     |
| ![Chigusa](assets/Chigusa.svg)       | [Chigusa]     | `#3A8FB7` | `oklch(61.57% 0.101 232.18)` | 67                     |
| ![brChigusa](assets/brChigusa.svg)   | brChigusa     | `#71DCEA` | `oklch(83.6% 0.101 206.67)`  | 45                     |
| ![Tsutsuji](assets/Tsutsuji.svg)     | [Tsutsuji]    | `#E03C8A` | `oklch(62.12% 0.21 356.23)`  | 198                    |
| ![brTsutsuji](assets/brTsutsuji.svg) | brTsutsuji    | `#FD67B8` | `oklch(72.45% 0.2 349.74)`   | 205                    |
| ![Kohaku](assets/Kohaku.svg)         | [Kohaku]      | `#CA7A2C` | `oklch(65.29% 0.134 60.34)`  | 172                    |
| ![Tamako](assets/Tamako.svg)         | [Tamako]      | `#F9BF45` | `oklch(83.66% 0.149 82.28)`  | 221                    |
| ![Black](./assets/Black.svg)         | Black/[Kachi] | `#08192D` | `oklch(21.09% 0.046 253.82)` | 234                    |
| ![brBlack](./assets/brBlack.svg)     | brBlack       | `#24384F` | `oklch(33.44% 0.048 251.83)` | 237                    |
| ![dimGrey](assets/dimGrey.svg)       | dimGrey       | `#5C7186` | `oklch(53.96% 0.041 248.6)`  | 242                    |
| ![Grey](assets/Grey.svg)             | Grey          | `#728A9E` | `oklch(62.18% 0.041 243.61)` | 245                    |
| ![brGrey](assets/brGrey.svg)         | brGrey        | `#83A2B7` | `oklch(69.62% 0.046 237.95)` | 247                    |
| ![White](assets/White.svg)           | White         | `#CCE0EC` | `oklch(89.59% 0.027 233.98)` | 253                    |
| ![brWhite](assets/brWhite.svg)       | brWhite       | `#DFF3FF` | `oklch(95.35% 0.027 230.91)` | 255                    |

[Kachi]: https://nipponcolors.com/#kachi
[Kurenai]: https://nipponcolors.com/#kurenai
[Nakabeni]: https://nipponcolors.com/#nakabeni
[Aomidori]: https://nipponcolors.com/#aomidori
[Kohaku]: https://nipponcolors.com/#kohaku
[Tamako]: https://nipponcolors.com/#tamako
[Ruri]: https://nipponcolors.com/#ruri
[Tsutsuji]: https://nipponcolors.com/#tsutsuji
[Chigusa]: https://nipponcolors.com/#chigusa

### Dark mode

![Dark mode palette](assets/dark-mode-palette.svg)

<details>
<summary>Figure of recommended color combinations for the dark mode</summary>

![Dark mode combinations](assets/dark-mode-combinations.svg)

</details>

<details>
<summary>Table of all of the colors used in the dark mode</summary>

| Color                                | Name          | Label    | Role                 |
| ------------------------------------ | ------------- | -------- | -------------------- |
| ![Nakabeni](assets/Nakabeni.svg)     | [Nakabeni]    | red      | Primary red          |
| ![brAomidori](assets/brAomidori.svg) | brAomidori    | green    | Primary green        |
| ![brRuri](assets/brRuri.svg)         | brRuri        | blue     | Primary blue         |
| ![brChigusa](assets/brChigusa.svg)   | brChigusa     | cyan     | Primary cyan         |
| ![brTsutsuji](assets/brTsutsuji.svg) | brTsutsuji    | magenta  | Primary magenta      |
| ![Tamako](assets/Tamako.svg)         | [Tamako]      | yellow   | Primary yellow       |
| ![Black](./assets/Black.svg)         | Black/[Kachi] | bg       | Primary background   |
| ![brBlack](assets/brBlack.svg)       | brBlack       | bg0      | Secondary background |
| ![brGrey](assets/brGrey.svg)         | brGrey        | fg0      | Secondary foreground |
| ![White](assets/White.svg)           | White         | fg       | Primary foreground   |
| ![Kurenai](assets/Kurenai.svg)       | [Kurenai]     | red0     | Secondary red        |
| ![Aomidori](assets/Aomidori.svg)     | [Aomidori]    | green0   | Secondary green      |
| ![Ruri](assets/Ruri.svg)             | [Ruri]        | blue0    | Secondary blue       |
| ![Chigusa](assets/Chigusa.svg)       | [Chigusa]     | cyan0    | Secondary cyan       |
| ![Tsutsuji](assets/Tsutsuji.svg)     | [Tsutsuji]    | magenta0 | Secondary magenta    |
| ![Kohaku](assets/Kohaku.svg)         | [Kohaku]      | yellow0  | Secondary yellow     |
| ![Grey](assets/Grey.svg)             | Grey          | ignore   | Ignorable            |

</details>

### Light mode

![Light mode palette](assets/light-mode-palette.svg)

<details>
<summary>Figure of recommended color combinations for the light mode</summary>

![Light mode combinations](assets/light-mode-combinations.svg)

</details>

<details>
<summary>Table of all of the colors used in the light mode</summary>

| Color                                | Name       | Label     | Role                 |
| ------------------------------------ | ---------- | --------- | -------------------- |
| ![Kurenai](assets/Kurenai.svg)       | [Kurenai]  | red       | Primary red          |
| ![Aomidori](assets/Aomidori.svg)     | [Aomidori] | green     | Primary green        |
| ![Ruri](assets/Ruri.svg)             | [Ruri]     | blue      | Primary blue         |
| ![Chigusa](assets/Chigusa.svg)       | [Chigusa]  | cyan      | Primary cyan         |
| ![Tsutsuji](assets/Tsutsuji.svg)     | [Tsutsuji] | magenta   | Primary magenta      |
| ![Kohaku](assets/Kohaku.svg)         | [Kohaku]   | yellow    | Primary yellow       |
| ![brWhite](./assets/brWhite.svg)     | brWhite    | bg        | Primary background   |
| ![White](assets/White.svg)           | White      | bg0       | Secondary background |
| ![dimGrey](assets/dimGrey.svg)       | dimGrey    | fg0       | Secondary foreground |
| ![brBlack](assets/brBlack.svg)       | brBlack    | fg        | Primary foreground   |
| ![Nakabeni](assets/Nakabeni.svg)     | [Nakabeni] | red0      | Secondary red        |
| ![brAomidori](assets/brAomidori.svg) | brAomidori | green0    | Secondary green      |
| ![brRuri](assets/brRuri.svg)         | brRuri     | blue0     | Secondary blue       |
| ![brChigusa](assets/brChigusa.svg)   | brChigusa  | cyan0     | Secondary cyan       |
| ![brTsutsuji](assets/brTsutsuji.svg) | brTsutsuji | magenta0  | Secondary magenta    |
| ![Tamako](assets/Tamako.svg)         | [Tamako]   | yellow0   | Secondary yellow     |
| ![Grey](assets/Grey.svg)             | Grey       | ignorable | Ignorable            |

</details>

## Ports

Lettepa is available for:

- [Vim](https://github.com/lettepa/vim)

## License

Lettepa is licensed under the [MIT License](LICENSE).
