import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { Box } from '@mui/material'

import { exerciseOptions, fetchData } from '../utils/fetchData'
import { Details } from '@mui/icons-material'

import Detail from '../Components/Detail'

const ExerciseDetails = () => {
  const [exerciseDetail, setexerciseDetail] = useState({});
  const { id } = useParams();

  useEffect(() => {
    const fetchExercisesData = async () => {
      const exerciseDbUrl = 'https://exercisedb.p.rapidapi.com';

      const exerciseDetailData = await fetchData(`${exerciseDbUrl}/exercises/exercise/${id}`, exerciseOptions);

      setexerciseDetail(exerciseDetailData);
    }

    fetchExercisesData();
  }, [id]);

  return (
    <Box>
      <Detail exerciseDetail={exerciseDetail}/>
    </Box>
  )
}

export default ExerciseDetails
