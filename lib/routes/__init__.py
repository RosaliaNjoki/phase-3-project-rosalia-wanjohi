from routes.students import students_bp
from routes.hostels import hostels_bp
from routes.rooms import rooms_bp
from routes.allocations import allocations_bp

#optional: create a list of dict of blueprints if you want to loop over them 
all_blueprints = [
    students_bp,
    hostels_bp,
    rooms_bp,
    allocations_bp

]