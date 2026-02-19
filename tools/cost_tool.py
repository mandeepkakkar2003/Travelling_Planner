def calculate_total_cost(flight_price: float, hotel_price: float, activity_cost: float) -> float:
    """
    Calculate the total cost of the trip.

    Args:
        flight_price (float): Cost of flight.
        hotel_price (float): Cost of hotel stay.
        activity_cost (float): Cost of activities.

    Returns:
        float: Total cost.
    """
    total = flight_price + hotel_price + activity_cost
    return total
