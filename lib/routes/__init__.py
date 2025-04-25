from .students import students_bp
from .hostels import hostels_bp
from .rooms import room_bp
from .allocations import allocations_bp

#optional: create a list of dict of blueprints if you want to loop over them 
all_blueprints = [
    students_bp
    hostels_bp
    rooms_bp
    allocations_bp

]