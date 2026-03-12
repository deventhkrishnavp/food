import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from cafe.models import Category, MenuItem, Review

def populate():
    # Categories
    categories = [
        'Fried Rice Combos', 'Chicken Dishes', 'Shawarma', 'Biryani', 'Snacks', 'Quick Bites', 'Fries', 'Combos & Packs', 'Fried Chicken'
    ]
    
    cat_objs = {}
    for cat_name in categories:
        cat, created = Category.objects.get_or_create(name=cat_name)
        cat_objs[cat_name] = cat
        print(f"Category '{cat_name}' {'created' if created else 'already exists'}")

    # Menu Items
    menu_items = [
        {
            'category': 'Fried Rice Combos',
            'name': 'Fried Rice Chicken Combo',
            'price': 180,
            'description': 'Delicious combo with fried rice, chicken pieces and special sauce.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png'
        },
        {
            'category': 'Fries',
            'name': 'Loaded Shawarma Fries',
            'price': 180,
            'description': 'Plates of loaded shawarma fries with special white sauce.',
            'is_featured': True,
            'image': 'menu_items/loaded_shawarma_fries.png'
        },
        {
            'category': 'Fries',
            'name': 'Loaded Fries Cheese with Chicken',
            'price': 150,
            'description': 'Crispy fries topped with melted cheese and seasoned chicken.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Shawarma',
            'name': 'Shawarma Roll Kuboos',
            'price': 80,
            'description': 'Classic shawarma roll in soft kuboos bread.',
            'is_featured': False,
            'image': 'menu_items/shawarma.png'
        },
        {
            'category': 'Shawarma',
            'name': 'Shawarma Roll Rumali',
            'price': 110,
            'description': 'Delicious shawarma wrapped in thin rumali roti.',
            'is_featured': False,
            'image': 'menu_items/shawarma.png'
        },
        {
            'category': 'Shawarma',
            'name': 'Shawarma Roll Rumali with Cheese',
            'price': 130,
            'description': 'Shawarma rumali with an extra layer of melted cheese.',
            'is_featured': False,
            'image': 'menu_items/shawarma.png'
        },
        {
            'category': 'Shawarma',
            'name': 'Plate Shawarma Kuboos',
            'price': 120,
            'description': 'Generous plate portion of shawarma served with kuboos.',
            'is_featured': False,
            'image': 'menu_items/shawarma.png'
        },
        {
            'category': 'Shawarma',
            'name': 'Plate Shawarma Rumali',
            'price': 130,
            'description': 'Plate portion of shawarma served with thin rumali roti.',
            'is_featured': False,
            'image': 'menu_items/shawarma.png'
        },
        {
            'category': 'Chicken Dishes',
            'name': 'Chicken Kothu Porotta',
            'price': 150,
            'description': 'Shredded porotta mixed with spicy chicken and eggs.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Chicken Dishes',
            'name': 'Chicken Strips',
            'price': 120,
            'description': 'Crispy golden fried chicken strips served with dip.',
            'is_featured': False,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Shawarma',
            'name': 'Special Shawarma',
            'price': 80,
            'description': 'Juicy chicken shawarma wrapped in soft bread with fresh veggies.',
            'is_featured': True,
            'image': 'menu_items/shawarma.png'
        },
        {
            'category': 'Biryani',
            'name': 'Chicken Biryani',
            'price': 160,
            'description': 'Authentic Kerala style chicken biryani with aromatic spices.',
            'is_featured': True,
            'image': 'menu_items/biryani.png'
        },
        {
            'category': 'Chicken Dishes',
            'name': 'Alfaham',
            'price': 220,
            'description': 'Grilled chicken marinated with Arabic spices.',
            'is_featured': False,
            'image': 'menu_items/biryani.png' # Placeholder
        },
        {
            'category': 'Combos & Packs',
            'name': 'Regular Meal',
            'price': 150,
            'description': '2 pcs Chicken, French Fries, Bun (1), Garlic sauce, Tomato Ketchup.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Combos & Packs',
            'name': 'Super Saver Pack',
            'price': 425,
            'description': '6 pcs Chicken, French Fries, Bun (3), Garlic sauce, Tomato Ketchup, Soft Drink 400 ML.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Combos & Packs',
            'name': 'Family Pack',
            'price': 699,
            'description': '10 pcs Chicken, French Fries, Bun (5), Garlic sauce, Tomato Ketchup, Soft Drink 700ML.',
            'is_featured': False,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Combos & Packs',
            'name': 'Party Pack',
            'price': 949,
            'description': '15 pcs Chicken, French Fries, Bun (7), Garlic sauce, Tomato Ketchup, Soft Drink 700ML.',
            'is_featured': False,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Combos & Packs',
            'name': 'Super Combo Offer (10pcs)',
            'price': 399,
            'description': '6pcs Strips + 4pcs Chicken, French Fries, Bun (3), Garlic sauce, Tomato Ketchup, Drink 400 ML.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Combos & Packs',
            'name': 'Super Combo Offer (15pcs)',
            'price': 599,
            'description': '5 pcs Chicken & 10 pcs Strips, Q Mandi Rice, French Fries, Bun (3), Garlic sauce, Tomato Ketchup, Drink 400 ML.',
            'is_featured': True,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Fried Chicken',
            'name': 'Boneless Chicken Strips (5 PCS)',
            'price': 99,
            'description': 'Tender boneless chicken strips fried to perfection.',
            'is_featured': False,
            'image': 'menu_items/fried_rice.png' # Placeholder
        },
        {
            'category': 'Fried Chicken',
            'name': 'Popcorn Chicken',
            'price': 90,
            'description': 'Bite-sized popcorn chicken, crispy and flavorful.',
            'is_featured': False,
            'image': 'menu_items/fried_rice.png' # Placeholder
        }
    ]

    for item in menu_items:
        obj, created = MenuItem.objects.get_or_create(
            name=item['name'],
            category=cat_objs[item['category']],
            defaults={
                'price': item['price'],
                'description': item['description'],
                'is_featured': item['is_featured'],
                'image': item['image']
            }
        )
        print(f"Menu Item '{item['name']}' {'created' if created else 'already exists'}")

    # Reviews
    reviews_data = [
        {'name': 'The Foodie Travelist', 'rating': 5, 'comment': 'There was nice and tasty food at an affordable rate. Very friendly customer service.'},
        {'name': 'Bobby Jose', 'rating': 5, 'comment': 'Amazing menu with many combos. Fried rice chicken combo and chicken kothu porotta were great.'},
        {'name': 'Anusha ANU', 'rating': 5, 'comment': 'Very tasty food with affordable rates. Excellent service and customer relations.'},
        {'name': 'Bijith Biju', 'rating': 5, 'comment': 'Tasty food, awesome service, and good atmosphere.'},
        {'name': 'Ashiq Hyder', 'rating': 5, 'comment': 'Value for money. Fried chicken for ₹50 tastes very good.'},
        {'name': 'Aneeshk Vijayan', 'rating': 5, 'comment': 'Delicious food in a calm atmosphere.'}
    ]

    for rev in reviews_data:
        Review.objects.get_or_create(
            name=rev['name'],
            comment=rev['comment'],
            defaults={'rating': rev['rating']}
        )
        print(f"Review from '{rev['name']}' created")

if __name__ == '__main__':
    populate()
