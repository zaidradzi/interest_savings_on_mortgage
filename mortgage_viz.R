library(ggplot2)
library(dplyr)

data <- read.csv("/Users/zaid/Downloads/Mortgage_Data.csv")
glimpse(data)

ggplot(data, aes(x = frequency, y = savings, color = scenario)) +
  geom_line(linewidth = 1.5, alpha = 0.9) +
  scale_x_continuous(name = "Frequency of Lump Sum Payments (years)") +
  scale_y_continuous(
    name = "Interest Savings ($)",
    breaks = c(10000, 20000, 30000, 40000),
    labels = c("10K", "20K", "30K", "40K")
  ) +
  scale_color_manual(
    values = c(
      "A" = "#3288bd",       
      "B" = "#d53e4f",       
      "C" = "#fee08b",      
      "D" = "#66c2a5",     
      "E" = "#f46d43",     
      "F" = "#e6f598",       
      "G" = "#abdda4",    
      "H" = "#fdae61" 
    ),
    labels = c(
      "A" = "A: $1,000 yearly",
      "B" = "B: $2,000 yearly",
      "C" = "C: $1,000 every 2 years",
      "D" = "D: $2,000 every 2 years",
      "E" = "E: $4,000 every 2 years",
      "F" = "F: $1,000 every 5 years",
      "G" = "G: $5,000 every 5 years",
      "H" = "H: $10,000 every 5 years"
    )
  ) +
  geom_text(
    aes(label = scenario), 
    data = data %>% group_by(scenario) %>% filter(frequency == max(frequency)),  # label at max frequency
    hjust = -1,     
    color = "black") +  
  theme_minimal() +
  labs(
    title = "Consistency Pays Off",
    subtitle = "Simulation for a $660K loan @ 3.00% p.a. for 35 years") +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    plot.subtitle = element_text(hjust = 0.5,margin = margin(b = 20)),
    legend.position = "bottom",
    legend.title = element_blank(),
    panel.grid.minor = element_blank(),
    axis.title.x = element_text(margin = margin(t = 20)),  
    axis.title.y = element_text(margin = margin(r = 20)) 
  )

