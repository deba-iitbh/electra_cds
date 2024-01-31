import React from 'react'
import { 
    Box,
    Container,
    Grid,
    styled,
    Typography,
} from '@mui/material'
import Title from './Title'
import { Fullscreen } from '@mui/icons-material'


const GetStarted = () => {
    

    const Box = styled(Grid) ({
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#302C42',
        width: '100'
    })
        const CustomTypography = styled(Typography) ({
        fontSize: '1.1rem',
        textAlign: 'start',
        lineHeight: '1.5',
        color: '#FFFFFF',
        marginTop: '1.5rem',
        marginBottom: '50px'
    })
       const CustomContainer = styled(Container) ({
         width: '100'
       })

    return (
                <Box component='article'
                sx={{
                    px: 4,
                }}
                >
                    <Typography variant='h3' color={'#9B91C6'}>
                        Why Choose Electra ?
                    </Typography>
                    
                    <CustomTypography>
                    ELECTRA offers an unparalleled shopping experience, providing not only top-tier products <br></br>
                    but also expert reviews, swift shipping, unbeatable prices, and a customer-centric approach.

                    </CustomTypography>
                </Box>
    )
}

export default GetStarted;