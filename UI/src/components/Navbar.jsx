import React from 'react'
import {
    AppBar,
    Toolbar,
    Box,
    Button,
    List,
    ListItem,
    Typography, 
    styled,
    ListItemButton,
    ListItemText,
} from '@mui/material';
// menu
// rotas
import { Link } from 'react-router-dom';


// personalizacao
const StyledToolbar = styled(Toolbar) ({
    display: 'flex',
    justifyContent: 'space-between',
});

const ListMenu = styled(List)(({ theme }) => ({
    display: 'none',
    [theme.breakpoints.up("sm")] : {
        display: "flex",
    },
}));

//rotas
const itemList = [
    {
        text: "Home",
        to: "/home"
    },
    {
        text: "Products",
        to: "/products"
    },
    {
      text: "Services",
      to: "/services" 
    },
];


const Navbar = () => {
    
    return (
        <AppBar 
        component="nav" 
        position="sticky"
        sx={{ 
            backgroundColor: '#302C42', 
        }}
        elevation={0}
        >
            <StyledToolbar >
                <Typography
                variant="h4"
                component="h2"
                sx={{color : '#9073AD'}}
                >
                    ELECTRA
                </Typography>
                <Box sx={{display: { xs: 'block', sm: 'none' } }}>
                </Box>
                <ListMenu>
                    {itemList.map( ( item ) => {
                        const { text } = item;
                        return(
                            <ListItem key={text}>
                                <ListItemButton component={Link} to={item.to}
                                sx={{
                                    color: '#9073AD',
                                    "&:hover": {
                                        backgroundColor: 'transparent',
                                        color: '#FFFFFF',
                                    }
                                }}
                                >
                                    <ListItemText primary={text} />
                                </ListItemButton>
                            </ListItem>
                        )
                    })}
                    <Button component={Link} to={'/login'}
                    sx={{
                        mr:2,
                        px: 3, 
                        py: 1,
                        fontSize: '0.9rem',
                        borderRadius: 5,
                        borderColor: '#14192d',
                        color: '#fff',
                        backgroundColor: '#14192d',
                        "&&:hover": {
                            backgroundColor: "#343a55"
                        },
                        "&&:focus": {
                            backgroundColor: "#343a55"
                        }
                    }}
                    >
                        Login
                    </Button>
                    <Button  component={Link} to={'/signup'}
                    sx={{
                        mr: 0,
                        px: 5, 
                        py: 1, 
                        fontSize: '0.9rem',
                        borderRadius: 5,
                        borderColor: '#14192d',
                        color: '#fff',
                        backgroundColor: '#14192d',
                        "&&:hover": {
                            backgroundColor: "#343a55"
                        },
                        "&&:focus": {
                            backgroundColor: "#343a55"
                        }
                    }}
                    > SignUp
                    </Button>       
                </ListMenu>           
            </StyledToolbar>
        </AppBar>
    )
}

export default Navbar;
