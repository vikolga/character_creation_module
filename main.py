from random import randint

# Глобальная константа
DEFAULT_ATTACK = 5  # значение стандартной атаки
DEFAULT_DEFENCE = 10  # значение стандартной защиты
DEFAULT_STAMINA = 80  # значение уровня стандартной выносливости


class Character:
    # Константа для диапазона очков урона в виде кортежа
    RANGE_VALUE_ATTACK = (1, 3)
    # Константа для диапазона очков защиты в виде кортежа
    RANGE_VALUE_DEFENCE = (1, 5)
    # константы умения и очков урона для базового класса
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки.
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}.')

    # Объявляем метод защиты.
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа
    """
    # Добавили словарь, в котором соотносится ввод пользователя
    # и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = ' '

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, за которого хочешь '
                               'играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, чтобы выбрать '
                               'другого персонажа ').lower
    return char_class


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    game_commands = {'attack': character.attack,
                     'defence': character.defence,
                     'special': character.special,
                    }
    cmd = ' '
    while cmd != 'skip':
        print('Потренируйся управлять своими навыками.')
        cmd = input('Введи одну из команд: attack — чтобы атаковать '
                    'противника, defence — чтобы блокировать атаку '
                    'противника или special — чтобы использовать '
                    'свою суперсилу. Если не хочешь тренироваться, '
                    'введи команду skip. Введи команду: ')
        if cmd in game_commands:
            print(game_commands[cmd])
    return 'Тренировка окончена.'


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
