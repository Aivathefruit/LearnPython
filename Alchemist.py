import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_initial_recipes():
    recipes = {}

    def add_recipe(a, b, result):
        recipes[(a, b)] = result
        recipes[(b, a)] = result

    add_recipe('огонь', 'вода', 'пар')
    add_recipe('огонь', 'земля', 'лава')
    add_recipe('огонь', 'воздух', 'молния')
    add_recipe('вода', 'земля', 'трава')
    add_recipe('вода', 'воздух', 'лед')
    add_recipe('земля', 'воздух', 'песок')
    add_recipe('лава', 'вода', 'камень')
    add_recipe('огонь', 'песок', 'стекло')
    add_recipe('песок', 'вода', 'металл')
    add_recipe('пар', 'вода', 'соль')
    add_recipe('соль', 'огонь', 'питер')
    add_recipe('трава', 'огонь', 'тюрьма')
    add_recipe('металл', 'энергия', 'электричество')
    add_recipe('электричество', 'стекло', 'лампа')
    add_recipe('пар', 'воздух', 'облако')
    add_recipe('облако', 'лед', 'дождь')
    add_recipe('трава', 'вода', 'дерево')
    add_recipe('дерево', 'металл', 'инструменты')
    add_recipe('камень', 'огонь', 'уголь')
    add_recipe('инструменты', 'молния', 'интелект')
    add_recipe('соль', 'камень', 'уран')
    add_recipe('уран', 'интелект', 'аэс')
    add_recipe('аэс', 'интелект', 'дядя петя')
    add_recipe('дядя петя', 'вода', 'бодяга')
    add_recipe('бодяга', 'интелект', 'посредственность')

    return recipes


class Alchemist:
    def __init__(self):
        self.elements = {'огонь', 'вода', 'земля', 'воздух'}
        self.recipes = create_initial_recipes()
        self.all_possible = self.elements | set(self.recipes.values())
        self.discovered_count = 0

    def get_new_combinations(self, elem1, elem2):
        result = self.recipes.get((elem1, elem2))
        if result and result not in self.elements:
            return result
        return None

    def show_elements(self):
        sorted_elements = sorted(self.elements)
        print(f"\n{'='*50}")
        print(f"Ваши элементы ({len(self.elements)}/{len(self.all_possible)}):")
        for i in range(0, len(sorted_elements), 5):
            print("  " + " | ".join(sorted_elements[i:i+5]))
        print(f"{'='*50}")

    def play(self):
        clear_console()
        print("=" * 50)
        print(" ДОБРО ПОЖАЛОВАТЬ В ИГРУ «АЛХИМИК»!")
        print("=" * 50)
        print("Смешивайте элементы, чтобы открыть новые.")
        print("Введите 'выход' чтобы завершить игру.\n")

        while len(self.elements) < len(self.all_possible):
            self.show_elements()

            print("\nПервый элемент (или 'выход'):")
            elem1 = input("> ").lower().strip()
            if elem1 == 'выход':
                break
            if elem1 not in self.elements:
                print(" Такого элемента нет в вашей коллекции!")
                input("Нажмите Enter для продолжения...")
                clear_console()
                continue

            print("Второй элемент:")
            elem2 = input("> ").lower().strip()
            if elem2 == 'выход':
                break
            if elem2 not in self.elements:
                print(" Такого элемента нет в вашей коллекции!")
                input("Нажмите Enter для продолжения...")
                clear_console()
                continue

            if elem1 == elem2:
                print("Нельзя смешивать элемент сам с собой!")
                input("Нажмите Enter для продолжения...")
                clear_console()
                continue

            result = self.get_new_combinations(elem1, elem2)
            clear_console()

            if result:
                self.elements.add(result)
                self.discovered_count += 1
                print(f" ОТКРЫТИЕ! {elem1} + {elem2} = {result.upper()}")
                print(f" Новый элемент добавлен в коллекцию!")
            else:
                print(f"{elem1} + {elem2} — ничего нового не происходит...")
                # Подсказка: может, уже открыт
                result_known = self.recipes.get((elem1, elem2))
                if result_known:
                    print(f"   (Элемент '{result_known}' уже есть в коллекции)")
                else:
                    print("   (Эта комбинация не даёт результата)")

            input("\nНажмите Enter для продолжения...")
            clear_console()

        if len(self.elements) == len(self.all_possible):
            print("\n" + "=" * 50)
            print("  ПОЗДРАВЛЯЕМ! ВЫ ОТКРЫЛИ ВСЕ ЭЛЕМЕНТЫ!")
            print("=" * 50)
            self.show_elements()
            print(f"\nВсего открыто элементов: {len(self.elements)}")
            print(f"Совершено открытий: {self.discovered_count}")
        else:
            print("\nИгра завершена. До новых алхимических открытий!")


if __name__ == '__main__':
    game = Alchemist()
    game.play()
