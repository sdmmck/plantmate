import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'plantmate.settings')
import django

django.setup()
from plantmateApp.models import Business, Plant


def populate():
    local_businesses = [
        {"title": "blooms",
         "url": "http://bloomsglasgow.co.uk/",
         "address": "182 Dumbarton Rd, Glasgow",
         "phone": "+44 (0)141 334 8552",
         "email": "INFO@BLOOMSGLASGOW.CO.UK",
         "hours": "MON - FRIDAY 9:00 - 5:30",
         "weekend_hours": "SAT 9:00 - 5:00",
         "lat": "55.870668",
         "long": "-4.300317"},
        {"title": "Apercu",
         "url": "https://www.instagram.com/apercuglasgow/?hl=en",
         "address": "617 Pollokshaws Road, Glasgow",
         "phone": "",
         "email": "",
         "hours": "Wednesday - Sunday 10.30-5.30",
         "weekend_hours": "",
         "lat": "55.837192",
         "long": "-4.269045"},
        {"title": "Roots, Fruits & Flowers",
         "url": "https://www.rootsfruitsflowershop.com",
         "address": "451 Great Western Road, Glasgow",
         "phone": "0141 334 3530",
         "email": "flowers@rootsfruitsandflowers.com",
         "hours": "Monday - Saturday : 09.00-5.00",
         "weekend_hours": "Sunday: Closed",
         "lat": "55.875217",
         "long": "-4.281234"}
    ]
    plants = [
        {"name": "Aloe Vera",
         "latin_name": "Aloe barbadensis miller",
         "size": "small",
         "characteristics": "Air purifying",
         "climate": "cool",
         "light": "sunny",
         "picture": "images/aloe-vera.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom",
         "description": "Aloe vera are known as Medicinal Aloe for the burn soothing gel within their fleshy leaves. Grown indoors or out, Aloe are an easy care plant and their narrow, water-holding leaves provide nice contrast to plants of broad or finely textured foliage. Plant them with other succulents for an attractive, low maintenance display."},

        {"name": "Banana Plant",
         "latin_name": "Musa tropicana",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "cool",
         "light": "sunny",
         "picture": "images/banana-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "Banana plants bring a tropical feel to any planting with their large leaves and interesting fruit and flowers. Most are grown purely as ornamentals, but some varieties do produce tasty fruit, in favorable climates. Keep sheltered from wind to protect the leaves from being shredded. Can be grown as houseplants as well."},

        {"name": "Cast Iron Plant",
         "latin_name": "Aspidistra",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "cool",
         "light": "shady",
         "picture": "images/cast-iron-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "Aspidistra’s bold, glossy foliage brings life to shaded areas. This is a reliable and versatile plant; slow-growing, easy to maintain, and excellent for growing in containers indoors or out. Aspidistra has been a popular houseplant ever since it was introduced from Asia to England during the mid-1800’s."},

        {"name": "Rose Painted Calathea",
         "latin_name": "Calathea roseopticta Dottie",
         "size": "Small",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/rose-painted-calathea.jpg",
         "pet": "yes",
         "room": "Kitchen/Bathroom",
         "description": "Calatheas come in a remarkable assortment of color blends ranging from green tones to burgundy and silver shades. The plant gets its common name \'Prayer Plant\' because the leaves on most selections fold closed at night similar to a pair of praying hands. A wonderful foliage plant that offers color and brightness for any room!"},

        {"name": "Chinese Evergreen",
         "latin_name": "Aglaeonema Maria",
         "size": "Medium",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "shady",
         "picture": "images/chinese-evergreen.jpg",
         "pet": "yes",
         "room": "Kitchen/Bathroom",
         "description": "Aglaonema are easy care selections perfect for bringing the beauty and health benefits of living plants into the home! Most varieties have variegated foliage that brightens any setting with its contrast of white and green. Allowing soil to dry a bit before watering, especially in winter, will keep Aglaonema at its healthiest."},

        {"name": "Chinese Money Plant",
         "latin_name": "Pilea peperomioides",
         "size": "small",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/chinese-money-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "A fun, funky plant with round, coin-shaped leaves that also earn it the name “pancake plant”. This Chinese native was discovered in 1946 by a Norwegian missionary. He brought the plant home to Norway and before long many people were growing and sharing money plants. The plants readily produce “babies” that can be removed to grow more plants. Grows tall with age into a more narrow, tree-like form"},

        {"name": "Dragon Plant",
         "latin_name": "Dracaena fragrans Lemon Lime",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "bright",
         "picture": "images/dragon-plant.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom",
         "description": "An attractive, upright plant with long leaves striped gold and green. Perfect for brightening corners and bringing vertical interest to mixed groupngs of houseplants."},

        {"name": "Golden Pothos",
         "latin_name": "Epipremnum aureum",
         "size": "Small",
         "characteristics": "Trailing",
         "climate": "warm",
         "light": "shady",
         "picture": "images/golden-pothos.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom",
         "description": "Truly one of the toughest, most popular and easy care houseplants! Golden Pothos sends out trailing stems of green leaves, variegated with white or gold. The variegation is more pronounced when they are grown in bright light, but they do adapt to lower light levels. Place where the vines can fall freely or trail along a shelf for the best effect."},

        {"name": "Swiss Cheese Plant",
         "latin_name": "Monstera deliciosa",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "shady",
         "picture": "images/swiss-cheese-plant.jpg",
         "pet": "no",
         "room": "Kitchen/Bathroom",
         "description": "Monstera are evergreen climbing shrubs with aerial roots, and usually ovate leaves which are often pinnately cut or lobed; arum-like flowerheads with white spathes arise from the leaf axils on mature plants. M. deliciosa is an evergreen shrub to 5m or more, climbing by aerial roots, with heart-shaped, pinnatisect and often perforated, glossy deep green leaves to 90cm; flower spathes 30cm, white, followed by cone-like cream fruit"},

        {"name": "Rattlesnake Plant",
         "latin_name": "Calathea Lancifolia",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/rattlesnake-plant.jpg",
         "pet": "yes",
         "room": "Kitchen/Bathroom",
         "description": "The rattlesnake plant is a decorative perennial with strappy, spotted leaves and deep purple undersides. Native to the Brazilian rainforest, rattlesnake plant thrives in moist, warm, semi-shady climates. If conditions are just right, the plant produces bright yellow-orange blooms in late spring and early summer. Rattlesnake plant is a real attention-getter, growing to heights of 30 inches and above."},

        {"name": "Straight-Cylindrical Snake Plant",
         "latin_name": "Sanseveieria cylindrica",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "shady",
         "picture": "images/straight-cylindrical-snake-plant.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom",
         "description": "Sansevieria cylindrica are particularly elegant house plants, with their smooth, round, spear-like foliage. This 'Straight' cultivar stands to attention and the striking grey-green variegation adds to its appeal as a perfect plant for any stylish, contemporary home."},

        {"name": "Spider Plant",
         "latin_name": "Clorophytum comosum",
         "size": "small",
         "characteristics": "Trailing",
         "climate": "cool",
         "light": "sunny",
         "picture": "images/spider-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "One of the most carefree plants around! Spider Plants easily adapt to indoor conditions and the soft, gently arched blades of foliage add a lush, relaxed feeling to any room. The perfect choice for bringing the vitality of nature indoors."},

        {"name": "String of Hearts",
         "latin_name": "Ceropegia woodii",
         "size": "small",
         "characteristics": "Trailing",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/string-of-hearts.jpg",
         "pet": "no",
         "room": "Kitchen/Bathroom",
         "description": "A gorgeous cascade of succulent heart-shaped leaves that seem to float along wiry stems. Each leaf is marbled with silver, giving the whole plant a silvery glow. Produces very unusual tubular flowers from summer into fall. This is a climbing, trailing plant in its native habitat of South Africa."},

        {"name": "Money Tree",
         "latin_name": "Pachira aquatica",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "shady",
         "picture": "images/money-tree.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom",
         "description": "A traditional housewarming or business opening gift in Asian cultures, Money Tree is a whimsical looking tree with a broad thick trunk and very slender branches sporting glossy leaves. Often multiple trunks are braided together increasing the thick to thin effect. Do not overwater and a money tree can prosper for many years."},

        {"name": "Parlour Palm",
         "latin_name": "Chamaedorea elegans",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "cool",
         "light": "shady",
         "picture": "images/parlour-palm.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "Frequently called Parlour Palm or Table Palm, indicating its popularity as a houseplant, this bushy palm has arching, airy fronds and requires little beyond moist soil. Arrange amongst broader leaved houseplants for a stylish display. Can be grown in the understory of other plants outdoors."},

        {"name": "Ponytail Palm",
         "latin_name": "Beaucarnea recurvata",
         "size": "Medium",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "shady",
         "picture": "images/ponytail-palm.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "Contrary to its common name, Pony Tail Palm is not a true palm. This plant is a native to dry regions of Mexico and its large stem base and root zone are specially adapted to storing water. A fun combination of unusual form and texture! "},

        {"name": "Spineless Yucca",
         "latin_name": "Yucca elephantipes",
         "size": "Large",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/spineless-yucca.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom",
         "description": "Yucca is a plant of strong lines and symmetry with its spiky leaves radiating out from the base in an attractive display of nature\'s architecture skills. Striking as a solo specimen in an entry way. Also provides nice contrast to groupings of softer houseplants."},

    ]

    for business in local_businesses:
        add_business(business)

    for plant in plants:
        add_plant(plant)


def add_business(business):
    p = Business.objects.get_or_create(name=business["title"],
                                       address=business["address"],
                                       lat=business["lat"],
                                       long=business["long"],
                                       phone=business["phone"],
                                       email=business["email"],
                                       hours=business["hours"],
                                       weekend_hours=business["weekend_hours"])[0]
    p.url = business["url"]
    p.save()
    return p


def add_plant(plant):
    plant = Plant.objects.get_or_create(name=plant["name"],
                                        latin_name=plant["latin_name"],
                                        size=plant["size"],
                                        characteristics=plant["characteristics"],
                                        climate=plant["climate"],
                                        light=plant["light"],
                                        picture=plant["picture"],
                                        pet=plant["pet"],
                                        room=plant["room"],
                                        description=plant["description"],
                                        )[0]
    plant.save()
    return plant


if __name__ == '__main__':
    print("Starting Plantmate population script...")
    populate()
